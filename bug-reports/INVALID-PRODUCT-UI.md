# Invalid Product ID Renders Undefined Product Data

## Summary
When a nonexistent product ID is opened, the Demoblaze product page renders
undefined product data instead of presenting a clear not-found state.

## Status / Classification
- Status: Confirmed through live-site reproduction
- Classification: UI defect in the third-party Demoblaze application
- Jira: Not filed; this is a local portfolio defect report

## Impact
Visitors who open an invalid product link see misleading product details.
The page does not clearly communicate that the requested product was not found.

## Expected Behavior
The page should display a clear not-found or invalid-product message. It should
not display undefined product details or offer an add-to-cart action for a
nonexistent product.

## Actual Behavior
The product API request returns HTTP 200 with the response body:

`{"errorMessage": "Not found."}`

Despite that response, the UI renders:
- Product title: `undefined`
- Product price: `$undefined *includes tax`
- An Add to cart action

HTTP 200 describes the response status; the response body contains the
application-level not-found result.

## Steps to Reproduce
1. Open `https://www.demoblaze.com/prod.html?idp_=999999`.
2. Wait for the product request to complete.
3. Inspect the product details displayed on the page.
4. Inspect the `POST /view` response in browser developer tools or the
   automated Playwright test.
5. Observe that the API reports `Not found.` while the UI renders undefined
   product details.

## Validation Evidence
The Playwright API test passed and confirmed:
- The `POST /view` response status is HTTP 200.
- The JSON response is `{"errorMessage": "Not found."}`.

The Playwright UI regression test reproduced the defect: the product-title
locator resolved to one element when the test expected zero. A separate
browser diagnostic also found one product-price element and one Add to cart
element for the invalid ID. The diagnostic did not verify the rendered
product-description text.

The UI regression test is marked as a strict expected failure (`xfail`) so
the known live-site defect remains visible without being misrepresented as a
passing UI behavior test.

## Environment
- Application: Demoblaze
- URL: `/prod.html?idp_=999999`
- Automation: Playwright with Chromium
- Test files: `ui-tests/tests/test_invalid_product_api.py` and
  `ui-tests/tests/test_invalid_product.py`

## Severity / Priority
- Severity: Medium
- Priority: Medium
- Rationale: Invalid product links display misleading data rather than a
  controlled not-found state.

## Evidence
The automated API and UI test results provide reproducible validation.
No Jira ticket or external issue link is claimed in this report.
