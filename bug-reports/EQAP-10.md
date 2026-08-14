# EQAP-10 — API /addtocart returns HTTP 500 when request ID is null

## Summary
The Demoblaze `POST /addtocart` API returns HTTP 500 Internal Server Error when the request `id` field is explicitly set to `null`.

## Impact
Invalid client input is not handled through controlled validation and can trigger a server-side error response.

## Expected Behavior
The API should reject a null request `id` with a controlled client-side validation response rather than returning HTTP 500.

## Actual Behavior
The API returned:

`500 Internal Server Error`

with the response body indicating an internal server error.

## Steps to Reproduce
1. Send `POST {{baseUrl}}/addtocart` in Postman.
2. Use a valid authentication token.
3. Use a valid product ID.
4. Set the request `id` field to `null`.
5. Send the request.
6. Observe the HTTP 500 response.

## Request Body

```json
{
  "id": null,
  "cookie": "{{authToken}}",
  "prod_id": {{productId}},
  "flag": true
}
```

## Validation Evidence
Postman validation tests passed:

- Null ID request returns HTTP 500 — **Passed**
- API returns Internal Server Error — **Passed**

The passing Postman assertions confirm that the observed response was reproducible and matched the documented test expectation.

## Environment
- Application: Demoblaze API
- Endpoint: `POST {{baseUrl}}/addtocart`
- Tool: Postman
- Browser/environment used during portfolio testing: Google Chrome

## Severity / Priority
- Severity: **Medium**
- Priority: **Medium**

## Jira
[EQAP-10 — API /addtocart returns HTTP 500 when request ID is null](https://demrkmoore.atlassian.net/browse/EQAP-10)

## Evidence
Request and response screenshots are attached to the Jira issue. Sensitive credentials and authentication values should not be committed to this public repository.
