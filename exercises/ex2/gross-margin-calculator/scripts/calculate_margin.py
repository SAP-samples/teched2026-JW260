#!/usr/bin/env python3
"""Calculate gross profit and gross margin from a JSON input file."""

import json
import sys
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path

MONEY_PLACES = Decimal("0.01")
PERCENT_PLACES = Decimal("0.01")
REQUIRED_FIELDS = ("revenue", "cost", "currency")


def validation_error(message):
    print(json.dumps({"error": message}), file=sys.stderr)
    return 2


def parse_decimal(value, field):
    if isinstance(value, bool):
        raise ValueError(f"{field} must be a number")
    try:
        number = Decimal(str(value))
    except (InvalidOperation, ValueError):
        raise ValueError(f"{field} must be a number")
    if not number.is_finite():
        raise ValueError(f"{field} must be a finite number")
    if number < 0:
        raise ValueError(f"{field} must not be negative")
    return number


def calculate(payload):
    missing = [field for field in REQUIRED_FIELDS if field not in payload or payload[field] in (None, "")]
    if missing:
        raise ValueError("missing required fields: " + ", ".join(missing))

    revenue = parse_decimal(payload["revenue"], "revenue")
    cost = parse_decimal(payload["cost"], "cost")
    currency = payload["currency"]
    if not isinstance(currency, str) or not currency.strip():
        raise ValueError("currency must be a nonempty string")

    gross_profit = (revenue - cost).quantize(MONEY_PLACES, rounding=ROUND_HALF_UP)
    warnings = []
    if revenue == 0:
        gross_margin = None
        warnings.append("Gross margin percent is undefined because revenue is zero.")
    else:
        gross_margin = ((revenue - cost) / revenue * Decimal("100")).quantize(
            PERCENT_PLACES, rounding=ROUND_HALF_UP
        )

    return {
        "gross_profit": format(gross_profit, ".2f"),
        "gross_margin_percent": None if gross_margin is None else format(gross_margin, ".2f"),
        "currency": currency,
        "warnings": warnings,
    }


def main(argv=None):
    args = sys.argv[1:] if argv is None else argv
    if len(args) != 1:
        return validation_error("usage: calculate_margin.py INPUT.json")

    try:
        payload = json.loads(Path(args[0]).read_text(encoding="utf-8"))
    except (OSError, UnicodeError) as exc:
        return validation_error(f"could not read input file: {exc}")
    except json.JSONDecodeError as exc:
        return validation_error(f"invalid JSON: {exc.msg}")

    if not isinstance(payload, dict):
        return validation_error("input must be one JSON object")

    try:
        result = calculate(payload)
    except ValueError as exc:
        return validation_error(str(exc))

    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
