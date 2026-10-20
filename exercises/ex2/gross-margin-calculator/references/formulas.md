# Gross Margin Formulas

## Formulas

- Gross profit = revenue - cost
- Gross margin percent = (gross profit / revenue) x 100
- Target revenue at a given cost and target margin = cost / (1 - target margin percent / 100)

No currency conversion is performed. Revenue and cost must use the same currency.

## Validation and rounding

- Revenue, cost, and currency are required.
- Revenue and cost must be numeric and cannot be negative.
- Round gross profit to two decimal places using decimal half-up rounding.
- Round gross margin percent to two decimal places using decimal half-up rounding.
- If revenue is zero, gross profit is still revenue minus cost, but gross margin percent is undefined. Return a null margin and a warning instead of dividing by zero.

## Worked examples

### Standard case

Revenue: 125000 EUR  
Cost: 87500 EUR  
Gross profit: 37500.00 EUR  
Gross margin: 30.00%

### Zero revenue

Revenue: 0 EUR  
Cost: 500 EUR  
Gross profit: -500.00 EUR  
Gross margin: undefined  
Warning: Gross margin percent is undefined because revenue is zero.

### Decimal rounding

Revenue: 100 EUR  
Cost: 66.666 EUR  
Gross profit: 33.33 EUR  
Gross margin: 33.33%
