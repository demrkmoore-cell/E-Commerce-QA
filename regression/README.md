# Regression Suite

This folder contains the high-value regression subset selected from the broader Demoblaze functional suite.

## Regression Focus

1. Registration / login smoke coverage
2. Product navigation and category selection
3. Product detail verification
4. Add product to cart
5. Remove product from cart
6. Multi-item cart totals
7. Cart persistence after refresh
8. Checkout launch with valid cart
9. Checkout field validation
10. Empty-cart behavior

## Execution Reference

See [`test-summary/execution-results.md`](../test-summary/execution-results.md) for the completed execution summary and defect findings.

## Automation Strategy

The first automation candidates should be critical, repeatable flows such as:

- Open home page
- Select product
- Add product to cart
- Verify cart item and price
- Verify cart total
- Open checkout
- Validate required checkout fields
- Complete a valid checkout flow

The suite should prioritize high-risk and frequently repeated scenarios rather than attempting to automate every manual test immediately.
