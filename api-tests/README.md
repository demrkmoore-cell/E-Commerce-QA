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

The collection contains **20 requests** organized into product, authentication, cart, and negative-test folders.

| Area | Checks |
|---|---|
| Catalog | HTTP status, non-empty product list, required product fields, positive prices |
| Product lookup | HTTP status, requested ID match, title and price |
| Sign up | HTTP status and absence of known signup-error responses |
| Login | HTTP status and authentication-token format |
| Add to cart | HTTP status and explicit item-added response |
| View cart | HTTP status, `Items` array, expected cart item present |
| Delete cart item | HTTP status, explicit deletion response, follow-up check that item is absent |
| Negative inputs | Null/empty cart ID, wrong ID type, invalid/missing token, malformed JSON, null/zero/invalid product IDs, unexpected fields, large and decimal IDs, Boolean ID |

## Negative-test interpretation

The collection records the observed response for each input. Some test cases intentionally assert only the observed HTTP status because a status such as `200` does not establish whether the API accepted, ignored, or correctly rejected the invalid input. Those cases are exploratory checks, not proof of correct business behavior and not automatically confirmed defects.

A test that asserts HTTP 500 for null/empty cart IDs is documenting the observed server error and supports investigation; it does not imply that a server error is acceptable expected product behavior. Confirmed defect reporting is maintained separately in the [EQAP-10 report](../bug-reports/EQAP-10.md) and the associated Jira issue.

## Security and test-data handling

- The committed collection contains no real account credentials or authentication token.
- Generated credentials and the cart ID are demo-only test data.
- Do not save real credentials or tokens into a shared/exported collection.
- The collection targets a public demo service; do not use it against systems without authorization.

## Evidence and limits

- The JSON collection structure is validated as part of repository review.
- **Latest verified live run (October 15, 2026): 21 HTTP requests executed, 37 assertions, 0 failed assertions.** The 21 requests include 20 saved collection requests plus one follow-up cart-verification request issued by the delete-item test. See the [successful Newman run](https://github.com/demrkmoore-cell/E-Commerce-QA/actions/runs/38799269716). A future run can fail if the external demo service changes or becomes unavailable; always use the current run as the source of truth.
- The collection does not replace the separate Python/Pytest API suite.
- API responses from the public service can vary over time; investigate failures and retain the run output rather than silently changing assertions to force a pass.

## Skills demonstrated

REST API testing, positive and negative testing, boundary/value-type testing, authentication and token validation, JSON request construction, Postman JavaScript assertions, test-data setup, reproducible execution, defect isolation, and evidence-based reporting.
