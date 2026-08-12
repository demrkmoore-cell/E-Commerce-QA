# EQAP-8 — Checkout Can Be Initiated With an Empty Cart

**Status:** Open  
**Severity:** High  
**Priority:** High  
**Test Type:** Negative / Checkout / Cart

## Summary
The checkout flow can be initiated when the shopping cart contains no products.

## Steps to Reproduce
1. Open the Cart page with no products in the cart.
2. Initiate the checkout / Place Order flow.
3. Observe whether the order dialog becomes available.

## Expected Result
Checkout should be unavailable when the cart is empty, or the application should clearly prevent order submission and display an appropriate validation message.

## Actual Result
The checkout flow can be initiated from an empty cart.

## Impact
This can permit an invalid order state to enter the checkout workflow without a purchasable item.

## Evidence
Observed during empty-cart negative testing. See Jira **EQAP-8**.
