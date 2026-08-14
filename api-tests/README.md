# API Testing

## Scope

This section documents API-level validation for the public Demoblaze e-commerce application using Postman.

**Base URL:** `https://api.demoblaze.com`

## API Test Objectives

- Validate successful product retrieval.
- Validate authentication and token handling.
- Validate shopping-cart requests with valid and invalid input.
- Validate HTTP status codes and response bodies.
- Validate error messages and server-side input handling.
- Use Postman assertions to make observed behavior reproducible.
- Link confirmed defects to Jira.
- Keep authentication credentials and tokens out of the repository.

## Executed Coverage

| Area | Endpoint / Operation | Status |
|---|---|---|
| Catalog | `GET /entries` | Verified |
| Authentication | `POST /login` | Verified |
| Cart | `POST /addtocart` | Verified — positive and negative coverage |
| Cart | `POST /viewcart` | Covered in collection |
| Cart | `POST /deleteitem` | Covered in collection |

## Negative Testing

The `/addtocart` negative suite was used to evaluate invalid and malformed request conditions, including:

- Invalid product IDs
- Null product IDs
- Zero product IDs
- Decimal product IDs
- Boolean product IDs
- Extremely large product IDs
- Missing product ID
- Missing cookie/token field
- Invalid authentication token
- Null request ID
- Empty request ID
- Unexpected request fields
- Malformed JSON

Each case was evaluated from the API's actual response rather than assuming that a negative request must return a specific status code.

## Confirmed API Defect

### EQAP-10 — Null request ID returns HTTP 500

`POST /addtocart` returns HTTP 500 Internal Server Error when the request `id` field is explicitly set to `null` while the authentication token and product ID are valid.

The Postman validation for this defect includes assertions confirming:

- HTTP 500 response
- `500 Internal Server Error` response content

The Jira issue contains the reproduction steps, expected/actual behavior, environment information, and two screenshots showing the request and response.

See [`../bug-reports/EQAP-10.md`](../bug-reports/EQAP-10.md) and [Jira EQAP-10](https://demrkmoore.atlassian.net/browse/EQAP-10).

## Observed Validation Behavior

Some invalid requests returned HTTP 200 with an error payload such as:

`{"errorMessage":"Bad parameter, token malformed."}`

These responses are documented as observed API behavior. They are not automatically classified as separate defects when they duplicate an already documented authentication/token-handling behavior.

## Postman Collection

The working collection is stored at:

[`Demoblaze-API-Tests.postman_collection.json`](Demoblaze-API-Tests.postman_collection.json)

The collection contains reusable environment variables such as `baseUrl`, `productId`, `cartId`, and authentication values. Secrets should be supplied through the local Postman environment rather than committed to GitHub.

## Validation Points

For each executed request, record:

1. HTTP method and endpoint.
2. Request headers and JSON body, excluding secrets.
3. HTTP status code.
4. Response body structure.
5. Required fields and data types.
6. Business-rule validation.
7. Response time where useful.
8. Postman assertion results.
9. Jira defect reference when behavior violates the expected result.

## Portfolio Value

This API work demonstrates practical QA skills in:

- REST API testing
- Positive and negative testing
- Boundary/value-type testing
- Authentication validation
- JSON request manipulation
- Postman scripting
- Response assertions
- Defect isolation
- Jira defect reporting
- Evidence-driven QA documentation
