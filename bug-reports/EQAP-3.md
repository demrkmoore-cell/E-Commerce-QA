# EQAP-3 — Registered User Cannot Log In After Successful Registration

**Status:** Open  
**Severity:** High  
**Priority:** High  
**Test Type:** Functional / Authentication  
**Related Area:** Registration / Login

## Summary
A user can complete registration successfully, but the newly registered account cannot subsequently authenticate through the Login flow.

## Preconditions
- Demoblaze is accessible.
- A unique test username is available.

## Steps to Reproduce
1. Open Demoblaze.
2. Select **Sign Up**.
3. Register a new user with valid test credentials.
4. Confirm the registration succeeds.
5. Open **Log in**.
6. Enter the newly registered username and password.
7. Submit the login request.

## Expected Result
The newly registered user should be able to log in successfully with the same valid credentials.

## Actual Result
The registered user cannot successfully log in after registration.

## Impact
Users may be unable to access an account immediately after creating it, breaking a critical registration-to-authentication workflow.

## Evidence
See Jira **EQAP-3** and the associated execution evidence.
