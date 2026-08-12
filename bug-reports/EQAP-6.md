# EQAP-6 — Checkout Accepts Invalid Expiration Month

**Status:** Open  
**Severity:** High  
**Priority:** High  
**Test Type:** Negative / Boundary / Checkout

## Summary
The checkout expiration-month field accepts invalid month values outside the valid `01–12` range.

## Steps to Reproduce
1. Add a product to the cart.
2. Select **Place Order**.
3. Enter otherwise valid customer information.
4. Enter `00` in the Month field.
5. Submit the order.
6. Repeat using `13` as the month.

## Expected Result
Values below `01` or above `12` should be rejected with a validation message and the order should not be submitted.

## Actual Result
Month `00` and month `13` were accepted during negative/boundary testing.

## Boundary Evidence
- `01` → accepted correctly
- `12` → accepted correctly
- `00` → incorrectly accepted
- `13` → incorrectly accepted

## Impact
Invalid expiration-month values can pass through a payment-related field without validation.

## Evidence
See Jira **EQAP-6** and checkout execution evidence.
