# EQAP-4 — Empty Shopping Cart Displays Blank Total

**Status:** Open  
**Severity:** Medium  
**Priority:** Medium  
**Test Type:** Functional / Cart

## Summary
When all products are removed from the shopping cart, the cart becomes empty but the Total field is blank instead of displaying a defined zero/empty-cart state.

## Steps to Reproduce
1. Add a product to the cart.
2. Open **Cart**.
3. Delete the product.
4. Observe the cart after the last item is removed.

## Expected Result
The cart should clearly indicate an empty state and the total should be handled consistently, such as displaying **0** or an explicitly defined empty-cart value.

## Actual Result
The cart is empty and the **Total** field is blank.

## Impact
The UI provides an ambiguous financial state and does not clearly communicate the cart's calculated total when no items remain.

## Evidence
The blank Total state was observed during execution and retested in TC-PROD-050. See Jira **EQAP-4**.
