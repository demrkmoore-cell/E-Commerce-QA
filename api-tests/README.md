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

- The JSON collection structure is validated as part of repository review.
- **Historical successful Newman run (October 15, 2026): 21 HTTP requests executed, 37 assertions, 0 failed assertions.** That run used an earlier collection version and is retained as historical evidence, not as proof that the current 48-request collection passes. On October 23, the latest audited Newman run executed all 48 requests and 144 assertions, with **1 failed assertion**: after Add to Cart returned HTTP 200 with an empty body, the subsequent View Cart response did not contain the newly added item. The other 143 assertions passed. The failure is retained as a real reproducibility finding against the public demo API rather than hidden by weakening the item-persistence assertion. See [that run](https://github.com/demrkmoore-cell/E-Commerce-QA/actions/runs/40011899249) and the [Postman/Newman workflow](https://github.com/demrkmoore-cell/E-Commerce-QA/actions/workflows/postman-api-tests.yml). The project owner separately reported that all 48 requests passed in Postman Desktop; the difference between local and CI results remains an open audit finding.
- The collection does not replace the separate Python/Pytest API suite.
- API responses from the public service can vary over time; investigate failures and retain the run output rather than silently changing assertions to force a pass.

## Skills demonstrated

REST API testing, positive and negative testing, boundary/value-type testing, authentication and token validation, JSON request construction, Postman JavaScript assertions, test-data setup, reproducible execution, defect isolation, and evidence-based reporting.
