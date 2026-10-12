#!/usr/bin/env python3
"""Rank open sales orders using deterministic workshop risk rules."""

import argparse
import csv
import datetime
import decimal
import json
from pathlib import Path

REQUIRED_COLUMNS = (
    "sales_order",
    "customer",
    "net_value",
    "currency",
    "requested_delivery_date",
    "overall_delivery_status",
    "delivery_block",
    "credit_block",
)
PRIORITIES = ("Critical", "High", "Medium", "Low")
TRUE_VALUES = {"true", "yes", "1"}
FALSE_VALUES = {"false", "no", "0"}
UNKNOWN_VALUES = {"unknown", "unresolved"}


class ValidationError(Exception):
    pass


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="input CSV file")
    parser.add_argument("--as-of", required=True, dest="as_of", help="analysis date in YYYY-MM-DD format")
    parser.add_argument("--output", required=True, type=Path, help="ranked output CSV file")
    return parser.parse_args(argv)


def parse_date(value, row_number, field):
    try:
        return datetime.datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError:
        raise ValidationError(f"row {row_number}, field {field}: expected YYYY-MM-DD, got {value!r}")


def parse_number(value, row_number, field):
    try:
        number = decimal.Decimal(value)
    except decimal.InvalidOperation:
        raise ValidationError(f"row {row_number}, field {field}: expected a number, got {value!r}")
    if not number.is_finite():
        raise ValidationError(f"row {row_number}, field {field}: expected a finite number, got {value!r}")
    return number


def parse_boolean(value, row_number, field):
    normalized = value.strip().lower()
    if normalized in TRUE_VALUES:
        return True
    if normalized in FALSE_VALUES:
        return False
    raise ValidationError(
        f"row {row_number}, field {field}: expected true/false, yes/no, or 1/0, got {value!r}"
    )


def parse_credit_block(value, row_number):
    normalized = value.strip().lower()
    if normalized in UNKNOWN_VALUES:
        return None
    return parse_boolean(value, row_number, "credit_block")


def priority_for(score):
    if score >= 70:
        return "Critical"
    if score >= 40:
        return "High"
    if score >= 20:
        return "Medium"
    return "Low"


def score_row(row, row_number, analysis_date):
    requested_date = parse_date(row["requested_delivery_date"].strip(), row_number, "requested_delivery_date")
    net_value = parse_number(row["net_value"].strip(), row_number, "net_value")
    delivery_block = parse_boolean(row["delivery_block"], row_number, "delivery_block")
    credit_block = parse_credit_block(row["credit_block"], row_number)
    complete = row["overall_delivery_status"].strip().lower() == "complete"

    score = 0
    reasons = []
    if credit_block is True:
        score += 50
        reasons.append("Credit block")
    elif credit_block is None:
        reasons.append("Credit status unresolved; no credit-block points awarded")
    if delivery_block:
        score += 40
        reasons.append("Delivery block")
    if not complete and requested_date < analysis_date:
        score += 30
        reasons.append("Requested delivery date is overdue")
    elif not complete and analysis_date <= requested_date <= analysis_date + datetime.timedelta(days=7):
        score += 20
        reasons.append("Requested delivery date is within 7 days")
    if net_value >= decimal.Decimal("50000"):
        score += 10
        reasons.append("Net value is at least 50000")

    ranked = dict(row)
    ranked["risk_score"] = str(score)
    ranked["priority"] = priority_for(score)
    ranked["credit_status_resolution"] = "unknown" if credit_block is None else "verified"
    ranked["risk_reasons"] = "; ".join(reasons) if reasons else "No risk rules matched"
    return ranked, requested_date


def process(input_path, output_path, analysis_date):
    try:
        input_file = input_path.open("r", encoding="utf-8-sig", newline="")
    except OSError as exc:
        raise ValidationError(f"could not read input file: {exc}")

    with input_file:
        reader = csv.DictReader(input_file)
        if reader.fieldnames is None:
            raise ValidationError("missing required columns: " + ", ".join(REQUIRED_COLUMNS))
        missing = [field for field in REQUIRED_COLUMNS if field not in reader.fieldnames]
        if missing:
            raise ValidationError("missing required columns: " + ", ".join(missing))

        ranked_rows = []
        for row_number, row in enumerate(reader, start=2):
            if None in row:
                raise ValidationError(f"row {row_number}: contains more values than the header")
            missing_values = [field for field in REQUIRED_COLUMNS if row[field] is None or not row[field].strip()]
            if missing_values:
                raise ValidationError(
                    f"row {row_number}: missing values for fields: " + ", ".join(missing_values)
                )
            ranked, requested_date = score_row(row, row_number, analysis_date)
            ranked_rows.append((ranked, requested_date))

    ranked_rows.sort(
        key=lambda item: (
            -int(item[0]["risk_score"]),
            item[1],
            item[0]["sales_order"],
        )
    )

    output_fields = list(reader.fieldnames) + [
        "risk_score",
        "priority",
        "credit_status_resolution",
        "risk_reasons",
    ]
    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with output_path.open("w", encoding="utf-8", newline="") as output_file:
            writer = csv.DictWriter(output_file, fieldnames=output_fields, lineterminator="\n")
            writer.writeheader()
            writer.writerows(item[0] for item in ranked_rows)
    except OSError as exc:
        raise ValidationError(f"could not write output file: {exc}")

    counts = {priority: 0 for priority in PRIORITIES}
    for ranked, _ in ranked_rows:
        counts[ranked["priority"]] += 1
    return {
        "order_count": len(ranked_rows),
        "priority_counts": counts,
        "unknown_credit_status_count": sum(
            ranked["credit_status_resolution"] == "unknown" for ranked, _ in ranked_rows
        ),
        "output_path": str(output_path),
    }


def main(argv=None):
    args = parse_args(argv)
    try:
        analysis_date = datetime.datetime.strptime(args.as_of, "%Y-%m-%d").date()
    except ValueError:
        argparse.ArgumentParser(add_help=False).exit(
            2, json.dumps({"error": "--as-of must use YYYY-MM-DD format"}) + "\n"
        )

    try:
        summary = process(args.input, args.output, analysis_date)
    except (ValidationError, csv.Error) as exc:
        argparse.ArgumentParser(add_help=False).exit(2, json.dumps({"error": str(exc)}) + "\n")

    print(json.dumps(summary, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
