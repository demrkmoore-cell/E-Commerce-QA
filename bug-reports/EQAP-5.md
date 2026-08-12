# EQAP-5 — Checkout Accepts Invalid Credit-Card Input

**Status:** Open  
**Severity:** High  
**Priority:** High  
**Test Type:** Negative / Boundary / Checkout

## Summary
The checkout form accepts invalid credit-card values that should fail validation.

## Preconditions
- At least one product is present in the cart.
- Place Order dialog is available.

## Steps to Reproduce
1. Add a product to the cart.
2. Select **Place Order**.
3. Enter otherwise valid customer information.
4. Enter an invalid credit-card value, such as `123`, alphabetic input, or a mixed-format value.
5. Submit the order.

## Expected Result
The credit-card field should reject invalid input and display a clear validation message. The order should not be submitted.

## Actual Result
Invalid credit-card input was accepted during negative testing.

## Impact
Weak payment-field validation can allow invalid transaction data to progress through checkout.

## Evidence
Observed during checkout negative testing. See Jira **EQAP-5**.
