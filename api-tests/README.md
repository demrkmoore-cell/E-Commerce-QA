# API Testing

## Scope

This section documents API-level validation for the Demoblaze e-commerce application.

The live application exposes a public catalog API at `https://api.demoblaze.com/`. A current request to `GET /entries` returned product records including product ID, category, title, price, description, and image path. citeturn180989view0

## API Test Objectives

- Validate successful product retrieval.
- Validate response structure and required fields.
- Validate product values against the UI/catalog expectations.
- Validate negative input handling for authentication, cart, and order operations where those endpoints are exercised.
- Validate HTTP status codes, response body structure, and error messages.
- Keep authentication/payment data out of the repository.

## Planned Endpoint Coverage

> Endpoint names for write operations should be confirmed against the browser's current Network traffic before execution. This repository intentionally avoids claiming execution for endpoints that have not yet been run and verified.

| Area | Endpoint / Operation | Status |
|---|---|---|
| Catalog | `GET /entries` | Verified live |
| Product | `POST /view` | Planned |
| Authentication | `POST /login` | Planned |
| Registration | `POST /signup` | Planned |
| Cart | `POST /addtocart` | Planned |
| Cart | `POST /viewcart` | Planned |
| Cart | `POST /deletecart` | Planned |
| Orders | `POST /placeorder` | Planned |

## Current Live Catalog Observation

`GET https://api.demoblaze.com/entries` currently returns product records with fields such as `id`, `cat`, `title`, `price`, `desc`, and `img`. The observed response includes examples such as Samsung Galaxy S6 at 360, Nokia Lumia 1520 at 820, Nexus 6 at 650, and Samsung Galaxy S7 at 800. citeturn180989view0

## Test Design

### Positive

- Successful catalog retrieval.
- Product retrieval by valid ID.
- Successful authentication with valid credentials.
- Successful registration with a unique username.
- Add a valid product to a cart.
- Retrieve an existing cart.
- Delete an existing cart item.
- Place an order with valid required data and a non-empty cart.

### Negative

- Invalid login credentials.
- Missing required authentication fields.
- Duplicate registration.
- Invalid product ID.
- Add-to-cart with a missing product identifier.
- Delete-cart for a missing item.
- Place order with empty cart.
- Place order with missing required order data.

### Validation Points

For each executed request, record:

1. HTTP method and endpoint.
2. Request headers and JSON body, excluding secrets.
3. HTTP status code.
4. Response body schema.
5. Required fields and data types.
6. Business-rule validation.
7. Response time where useful.
8. Defect reference when behavior violates the expected result.

## Execution Status

**Current API execution:** 1 live catalog endpoint verified. Remaining cases are planned and should be executed in Postman before being marked PASS/FAIL.
