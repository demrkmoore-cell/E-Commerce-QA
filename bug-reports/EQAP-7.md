# EQAP-7 — Checkout Accepts Invalid or Expired Expiration Year

**Status:** Open  
**Severity:** High  
**Priority:** High  
**Test Type:** Negative / Boundary / Checkout

## Summary
The checkout expiration-year field accepts invalid and expired year values that should fail validation.

## Steps to Reproduce
1. Add a product to the cart.
2. Select **Place Order**.
3. Enter otherwise valid customer information.
4. Enter an invalid year such as `0000`.
5. Submit the order.
6. Repeat using an expired year such as `2020`.

## Expected Result
The year should be valid and current/future according to the application's defined payment rules. Invalid or expired values should be rejected.

## Actual Result
Year `0000` and expired year `2020` were accepted during negative testing.

## Boundary Evidence
- `0000` → incorrectly accepted
- `2020` → incorrectly accepted
- `2026` → accepted as valid test data

## Impact
Invalid or expired payment expiration data can progress through checkout without appropriate validation.

## Evidence
See Jira **EQAP-7** and checkout execution evidence.
