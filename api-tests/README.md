# Postman API Testing

## Scope

This collection exercises the public Demoblaze e-commerce API at `https://api.demoblaze.com`. It is a portfolio demonstration against a third-party demo service, not a production API or a service controlled by this repository.

## Run the collection

### In Postman

1. Import `Demoblaze-API-Tests.postman_collection.json`.
2. Use the collection's default variables or set `baseUrl` to `https://api.demoblaze.com`.
3. Do not create environment variables with the same names as the collection variables unless you intend to override them. Postman environment values take precedence over collection values.
4. Run the entire collection in order. The collection-level pre-request script creates a unique demo username, password, and cart ID at runtime when those values are blank.
5. The Authentication folder signs up before logging in. The login test stores the returned token in the collection variable `authToken`. The cart flow then adds an item, checks the cart, and deletes the item.
6. Review each request's **Test Results** and the collection run summary. An HTTP status by itself does not prove that a business operation succeeded.

### In CI with Newman

The workflow [Postman API Collection](../.github/workflows/postman-api-tests.yml) runs the collection with Newman on pushes/pull requests that affect the collection or workflow, and can also be started manually from GitHub Actions.

- [View recent Postman/Newman runs](https://github.com/demrkmoore-cell/E-Commerce-QA/actions/workflows/postman-api-tests.yml)
- The workflow output is the source of truth for whether the current collection passed against the live demo API.
- The external service may be unavailable or change behavior; a failed run must be investigated rather than reported as a successful test.

## Collection coverage

The collection contains **48 requests**: 3 authentication requests, 2 catalog requests, 39 cart/negative-input requests, and 4 standalone regression requests at the collection root. The exact count is checked against the committed JSON during repository review.

| Area | Checks |
|---|---|
| Catalog | HTTP status, non-empty product list, required product fields, positive prices |
| Catalog field validation | HTTP status, required product fields, positive prices |
| Sign up | HTTP status and absence of known signup-error responses |
| Login | HTTP status and authentication-token format |
| Add to cart | HTTP status, empty success response, response-time limit |
| View cart | HTTP status, `Items` array, expected product present; captures the returned cart-item ID for deletion |
| Delete cart item | Uses the cart-item ID returned by View Cart, validates deletion response, and verifies the cart state afterward |
| Negative inputs | Null/empty cart ID, wrong ID type, invalid/missing token, malformed JSON, null/zero/invalid product IDs, unexpected fields, large and decimal IDs, Boolean ID |

## Negative-test interpretation

The collection records the observed response for each input. Some test cases intentionally assert only the observed HTTP status because a status such as `200` does not establish whether the API accepted, ignored, or correctly rejected the invalid input. Those cases are exploratory checks, not proof of correct business behavior and not automatically confirmed defects.

Invalid-input tests accept documented response variants where the public service has returned different statuses/bodies across runs. They log the observed response and retain time-limit assertions; this does not imply that an HTTP 500 or ignored invalid input is acceptable expected product behavior. Confirmed defect reporting is maintained separately in the [EQAP-10 report](../bug-reports/EQAP-10.md) and the associated Jira issue.

## Security and test-data handling

- The committed collection contains no real account credentials or authentication token.
- Generated credentials and the cart ID are demo-only test data.
- Do not save real credentials or tokens into a shared/exported collection.
- The collection targets a public demo service; do not use it against systems without authorization.

## Evidence and limits

- The committed JSON collection is validated during repository review.
- **Latest successful Newman run (October 24, 2026, commit `d52f48c`): 48 HTTP requests, 144 assertions, 0 failures.** The [Postman/Newman GitHub Actions run](https://github.com/demrkmoore-cell/E-Commerce-QA/actions/runs/40112769159) passed against the public Demoblaze API. The same collection version also passed a local Newman run. The cart lifecycle was verified by adding an item, confirming it appeared in View Cart, deleting it, and confirming it was absent afterward.
- Earlier CI runs on previous commits failed when the added cart item did not appear in View Cart. Those failures were investigated; the cart owner ID and item lifecycle assertions were corrected, and the successful run above verifies the updated commit. The earlier [October 23 failed run](https://github.com/demrkmoore-cell/E-Commerce-QA/actions/runs/40011899249) remains available as historical evidence and is not the current result.
- The October 15, 2026 run (21 requests, 37 assertions, 0 failures) used an earlier collection version and is retained as historical evidence only.
- A passing test suite confirms that its assertions passed against the observed API responses; it does not prove the public API is defect-free. Several invalid-input tests record observed response behavior, and some cases return HTTP 200 or HTTP 500 for invalid inputs. These observations should not be interpreted as proof that the API handled those inputs correctly.
- The collection does not replace the separate Python/Pytest API suite.
- The public demo service can change or become unavailable; investigate future failures and retain run output rather than weakening assertions just to force a pass.

## Skills demonstrated

REST API testing, positive and negative testing, boundary/value-type testing, authentication and token validation, JSON request construction, Postman JavaScript assertions, test-data setup, reproducible execution, defect isolation, and evidence-based reporting.
