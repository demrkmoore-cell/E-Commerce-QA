# Demoblaze Functional Test Cases

## Project Information

| Field | Value |
|---|---|
| Application | Demoblaze |
| Project | E-Commerce QA Portfolio |
| Jira Project | EQAP |
| Jira Task | EQAP-2 — Create Functional Test Cases |
| Test Type | Functional |
| Test Suite Status | In Progress |
| Owner | DeMarko Moore |

## Test Case Format

Each test case contains:

- Test ID
- Feature
- Scenario
- Priority
- Preconditions
- Test Data
- Test Steps
- Expected Result
- Actual Result
- Status

**Execution status:** Not Run unless otherwise documented.

---

# 1. Registration / User Account

## TC-REG-001 — Register a new user with valid credentials

| Field | Details |
|---|---|
| Feature | Registration |
| Priority | High |
| Preconditions | Demoblaze is accessible and the Sign Up function is available |
| Test Data | Unique username and valid password |
| Steps | 1. Open Demoblaze. 2. Select Sign Up. 3. Enter a unique username. 4. Enter a password. 5. Submit the registration form. |
| Expected Result | The application accepts the registration request and provides the appropriate success response. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-REG-002 — Attempt registration with an existing username

| Field | Details |
|---|---|
| Feature | Registration |
| Priority | High |
| Preconditions | A Demoblaze account already exists for the test username |
| Test Data | Existing username and password |
| Steps | 1. Open Sign Up. 2. Enter an existing username. 3. Enter a password. 4. Submit. |
| Expected Result | The application rejects the duplicate registration and displays an appropriate message. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-REG-003 — Register with an empty username

| Field | Details |
|---|---|
| Feature | Registration |
| Priority | High |
| Preconditions | Sign Up dialog is open |
| Test Data | Username: blank; Password: valid test value |
| Steps | 1. Leave username blank. 2. Enter a password. 3. Submit registration. |
| Expected Result | The application prevents invalid registration and provides appropriate feedback. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-REG-004 — Register with an empty password

| Field | Details |
|---|---|
| Feature | Registration |
| Priority | High |
| Preconditions | Sign Up dialog is open |
| Test Data | Username: unique test value; Password: blank |
| Steps | 1. Enter a unique username. 2. Leave password blank. 3. Submit registration. |
| Expected Result | The application prevents invalid registration and provides appropriate feedback. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-REG-005 — Register with both username and password empty

| Field | Details |
|---|---|
| Feature | Registration |
| Priority | High |
| Preconditions | Sign Up dialog is open |
| Test Data | Username: blank; Password: blank |
| Steps | 1. Leave both fields blank. 2. Submit registration. |
| Expected Result | Registration is not completed and appropriate feedback is provided. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-REG-006 — Register with a username containing spaces

| Field | Details |
|---|---|
| Feature | Registration |
| Priority | Medium |
| Preconditions | Sign Up dialog is open |
| Test Data | Username containing leading, trailing, or internal spaces |
| Steps | 1. Enter the test username. 2. Enter a valid password. 3. Submit registration. |
| Expected Result | The application handles whitespace according to its implemented validation rules and does not create an unintended account. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-REG-007 — Register using special characters in username

| Field | Details |
|---|---|
| Feature | Registration |
| Priority | Medium |
| Preconditions | Sign Up dialog is open |
| Test Data | Username containing supported/unsupported special characters |
| Steps | 1. Enter the test username. 2. Enter a valid password. 3. Submit registration. |
| Expected Result | The application handles the username according to its implemented validation behavior. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-REG-008 — Verify registration dialog can be cancelled

| Field | Details |
|---|---|
| Feature | Registration |
| Priority | Medium |
| Preconditions | Sign Up dialog is open |
| Test Data | None |
| Steps | 1. Open Sign Up. 2. Enter test information if desired. 3. Select Cancel/close control. |
| Expected Result | The registration dialog closes without creating an account. |
| Actual Result | Not Run |
| Status | Not Run |

---

# 2. Login

## TC-LOGIN-001 — Login with valid credentials

| Field | Details |
|---|---|
| Feature | Login |
| Priority | Critical |
| Preconditions | A valid Demoblaze account exists |
| Test Data | Valid registered username and password |
| Steps | 1. Open Demoblaze. 2. Select Log in. 3. Enter valid credentials. 4. Submit. |
| Expected Result | The user is authenticated and the application displays the authenticated-user state. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-LOGIN-002 — Login with an incorrect password

| Field | Details |
|---|---|
| Feature | Login |
| Priority | High |
| Preconditions | A valid username exists |
| Test Data | Valid username; incorrect password |
| Steps | 1. Open Log in. 2. Enter the valid username. 3. Enter an incorrect password. 4. Submit. |
| Expected Result | Authentication fails and the application displays appropriate feedback. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-LOGIN-003 — Login with an unregistered username

| Field | Details |
|---|---|
| Feature | Login |
| Priority | High |
| Preconditions | Test username does not exist |
| Test Data | Unregistered username and test password |
| Steps | 1. Open Log in. 2. Enter an unregistered username. 3. Enter a password. 4. Submit. |
| Expected Result | Authentication fails and appropriate feedback is displayed. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-LOGIN-004 — Login with empty username

| Field | Details |
|---|---|
| Feature | Login |
| Priority | High |
| Preconditions | Login dialog is open |
| Test Data | Username: blank; Password: valid test value |
| Steps | 1. Leave username blank. 2. Enter password. 3. Submit. |
| Expected Result | Login does not succeed and the application handles the missing username appropriately. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-LOGIN-005 — Login with empty password

| Field | Details |
|---|---|
| Feature | Login |
| Priority | High |
| Preconditions | Login dialog is open |
| Test Data | Username: valid; Password: blank |
| Steps | 1. Enter username. 2. Leave password blank. 3. Submit. |
| Expected Result | Login does not succeed and the application handles the missing password appropriately. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-LOGIN-006 — Login with both fields empty

| Field | Details |
|---|---|
| Feature | Login |
| Priority | High |
| Preconditions | Login dialog is open |
| Test Data | Username: blank; Password: blank |
| Steps | 1. Leave both fields blank. 2. Submit login. |
| Expected Result | Authentication does not occur and appropriate feedback is provided. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-LOGIN-007 — Verify logout after successful login

| Field | Details |
|---|---|
| Feature | Login / Logout |
| Priority | Critical |
| Preconditions | User is successfully logged in |
| Test Data | Valid registered account |
| Steps | 1. Log in. 2. Verify authenticated-user state. 3. Select Log out. |
| Expected Result | The authenticated-user state ends and the application returns to the logged-out state. |
| Actual Result | Not Run |
| Status | Not Run |

---

# Initial Coverage Summary

| Feature | Test Cases |
|---|---:|
| Registration | 8 |
| Login / Logout | 7 |
| **Total** | **15** |

