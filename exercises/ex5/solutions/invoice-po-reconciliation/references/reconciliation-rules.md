# Reconciliation Rules

## Price deviation tolerance

- `match` — absolute percentage difference between invoiced and PO unit price is within **2.00%** (inclusive).
- `price_deviation` — absolute percentage difference exceeds 2.00%.

Formula:

```
price_deviation_pct = abs(invoiced_unit_price - po_unit_price) / po_unit_price × 100
```

Round to two decimal places. If `po_unit_price` is zero and `invoiced_unit_price` is also zero, treat as `match`. If `po_unit_price` is zero and `invoiced_unit_price` is nonzero, classify as `price_deviation`.

## Quantity deviation

Status is `quantity_deviation` when invoiced quantity differs from PO quantity and price is within tolerance. When both price and quantity differ, status is `price_deviation` — record the quantity difference in the `Note` field.

## Matching

Match invoice lines to PO items by description (case-insensitive). Do not use fuzzy or partial matching.

- Invoice line with no matching PO item → `not_in_po`
- PO item with no matching invoice line → `not_invoiced`

## Line total validation

A line total is valid when `abs(line_total - quantity × unit_price) ≤ 0.01`. Report any invalid line and ask the user to confirm or correct before continuing.

## PO line value

`PO line value = NetPriceAmount / NetPriceQuantity × OrderQuantity`

## Overall status

`MATCH` requires net deviation of 0.00 and no lines with any deviation or mismatch status. Any other result is `REVIEW REQUIRED`.

## Rounding

All monetary amounts and percentages: two decimal places, half-up rounding.

## PO fixture format

When the SAP-published S/4HANA capability is unavailable, the user may supply a JSON fixture:

```json
{
  "PurchaseOrder": "4500000000",
  "Supplier": "USSU-V100",
  "PurchasingOrganization": "1710",
  "DocumentCurrency": "EUR",
  "CreationDate": "2023-08-10",
  "Items": [
    {
      "PurchaseOrderItem": "00010",
      "PurchaseOrderItemText": "Microsoft Surface Laptop 3 - Platinum 13.5in",
      "OrderQuantity": 1,
      "OrderQuantityUnit": "EA",
      "NetPriceAmount": 869.00,
      "NetPriceQuantity": 1,
      "DocumentCurrency": "EUR"
    }
  ]
}
```
