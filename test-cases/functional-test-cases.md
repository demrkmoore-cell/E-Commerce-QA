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

# 3. Navigation & Categories

## TC-NAV-001 — Verify the home page loads successfully

| Field | Details |
|---|---|
| Feature | Navigation |
| Priority | Critical |
| Preconditions | Demoblaze is accessible |
| Test Data | None |
| Steps | 1. Navigate to the Demoblaze home page. 2. Wait for the page to load. |
| Expected Result | The home page loads successfully and the primary navigation and product content are displayed. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-NAV-002 — Verify the site logo returns the user to the home page

| Field | Details |
|---|---|
| Feature | Navigation |
| Priority | High |
| Preconditions | User is on a page other than the home page |
| Test Data | None |
| Steps | 1. Navigate to a product or category page. 2. Select the Demoblaze logo/home control. |
| Expected Result | The user is returned to the home page. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-NAV-003 — Navigate from home page to a product detail page

| Field | Details |
|---|---|
| Feature | Navigation |
| Priority | High |
| Preconditions | Home page is loaded and products are displayed |
| Test Data | Any available product |
| Steps | 1. Select a product from the product listing. |
| Expected Result | The selected product detail page opens and displays information for the selected product. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-NAV-004 — Navigate between product pages using browser navigation

| Field | Details |
|---|---|
| Feature | Navigation |
| Priority | Medium |
| Preconditions | User has navigated from the home page to a product detail page |
| Test Data | Any available product |
| Steps | 1. Open a product detail page. 2. Use the browser Back control. 3. Use the browser Forward control. |
| Expected Result | Browser navigation returns the user to the previously visited pages without unexpected errors. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-NAV-005 — Refresh the home page

| Field | Details |
|---|---|
| Feature | Navigation |
| Priority | Medium |
| Preconditions | Home page is loaded |
| Test Data | None |
| Steps | 1. Load the home page. 2. Refresh the browser page. |
| Expected Result | The page reloads successfully and the expected navigation and product content remain available. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-NAV-006 — Verify primary navigation links are accessible

| Field | Details |
|---|---|
| Feature | Navigation |
| Priority | High |
| Preconditions | Home page is loaded |
| Test Data | None |
| Steps | 1. Review the primary navigation controls. 2. Select each available navigation option. |
| Expected Result | Each available navigation control responds and opens the expected destination or interface. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-NAV-007 — Select Phones category

| Field | Details |
|---|---|
| Feature | Categories |
| Priority | High |
| Preconditions | Home page is loaded |
| Test Data | Phones category |
| Steps | 1. Select the Phones category. |
| Expected Result | The product listing updates to display products belonging to the Phones category. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-NAV-008 — Select Laptops category

| Field | Details |
|---|---|
| Feature | Categories |
| Priority | High |
| Preconditions | Home page is loaded |
| Test Data | Laptops category |
| Steps | 1. Select the Laptops category. |
| Expected Result | The product listing updates to display products belonging to the Laptops category. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-NAV-009 — Select Monitors category

| Field | Details |
|---|---|
| Feature | Categories |
| Priority | High |
| Preconditions | Home page is loaded |
| Test Data | Monitors category |
| Steps | 1. Select the Monitors category. |
| Expected Result | The product listing updates to display products belonging to the Monitors category. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-NAV-010 — Switch between product categories

| Field | Details |
|---|---|
| Feature | Categories |
| Priority | High |
| Preconditions | Home page is loaded |
| Test Data | Phones, Laptops, and Monitors |
| Steps | 1. Select Phones. 2. Verify the displayed products. 3. Select Laptops. 4. Verify the displayed products. 5. Select Monitors. 6. Verify the displayed products. |
| Expected Result | Each category selection updates the displayed products appropriately without displaying products from an unrelated category. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-NAV-011 — Return from a category to the home/product listing

| Field | Details |
|---|---|
| Feature | Categories / Navigation |
| Priority | Medium |
| Preconditions | A product category is selected |
| Test Data | Any category |
| Steps | 1. Select a category. 2. Use the available home/navigation control. |
| Expected Result | The user returns to the expected product listing/home view. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-NAV-012 — Verify category selection does not create an application error

| Field | Details |
|---|---|
| Feature | Categories |
| Priority | Medium |
| Preconditions | Home page is available |
| Test Data | Each available product category |
| Steps | 1. Select each available category. 2. Observe the page after each selection. |
| Expected Result | The category loads without an application crash, broken page, or unexpected error message. |
| Actual Result | Not Run |
| Status | Not Run |

---

# Navigation & Categories Coverage Summary

| Feature | Test Cases |
|---|---:|
| Navigation | 6 |
| Categories | 6 |
| **New Cases** | **12** |
| Previous Cases | 15 |
| **Total Cases** | **27** |

---

# 4. Product Details

## TC-PROD-001 — Open a product detail page

| Field | Details |
|---|---|
| Feature | Product Details |
| Priority | Critical |
| Preconditions | Home page is loaded and products are displayed |
| Test Data | Any available product |
| Steps | 1. Select a product from the product listing. |
| Expected Result | The selected product detail page opens successfully. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-PROD-002 — Verify product name is displayed

| Field | Details |
|---|---|
| Feature | Product Details |
| Priority | High |
| Preconditions | Product detail page is open |
| Test Data | Any available product |
| Steps | 1. Open a product detail page. 2. Locate the product name. |
| Expected Result | The product name is displayed clearly and corresponds to the selected product. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-PROD-003 — Verify product price is displayed

| Field | Details |
|---|---|
| Feature | Product Details |
| Priority | High |
| Preconditions | Product detail page is open |
| Test Data | Any available product |
| Steps | 1. Open a product detail page. 2. Locate the displayed price. |
| Expected Result | A product price is displayed and is associated with the selected product. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-PROD-004 — Verify product description is displayed

| Field | Details |
|---|---|
| Feature | Product Details |
| Priority | High |
| Preconditions | Product detail page is open |
| Test Data | Any available product |
| Steps | 1. Open a product detail page. 2. Locate the product description. |
| Expected Result | The product description is displayed and provides information about the selected product. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-PROD-005 — Verify product image is displayed

| Field | Details |
|---|---|
| Feature | Product Details |
| Priority | Medium |
| Preconditions | Product detail page is open |
| Test Data | Any available product |
| Steps | 1. Open a product detail page. 2. Observe the product image area. |
| Expected Result | The product image loads and is displayed without a broken-image indicator. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-PROD-006 — Verify product information matches the selected product

| Field | Details |
|---|---|
| Feature | Product Details |
| Priority | High |
| Preconditions | Product listing is displayed |
| Test Data | Any available product |
| Steps | 1. Record the product name from the listing. 2. Select the product. 3. Compare the product name on the detail page. |
| Expected Result | The product detail page corresponds to the product selected from the listing. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-PROD-007 — Verify product price consistency

| Field | Details |
|---|---|
| Feature | Product Details |
| Priority | Critical |
| Preconditions | Product listing is displayed |
| Test Data | Any available product |
| Steps | 1. Record the displayed product price from the listing. 2. Open the product detail page. 3. Compare the displayed prices. |
| Expected Result | The product price is consistent between the product listing and detail page, unless a documented application behavior indicates otherwise. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-PROD-008 — Add a product to the cart from its detail page

| Field | Details |
|---|---|
| Feature | Product Details / Cart |
| Priority | Critical |
| Preconditions | Product detail page is open |
| Test Data | Any available product |
| Steps | 1. Open a product detail page. 2. Select Add to cart. 3. Navigate to the cart. |
| Expected Result | The selected product is added to the cart with the correct product information and price. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-PROD-009 — Verify add-to-cart confirmation behavior

| Field | Details |
|---|---|
| Feature | Product Details / Cart |
| Priority | High |
| Preconditions | Product detail page is open |
| Test Data | Any available product |
| Steps | 1. Select Add to cart. 2. Observe the application's response. |
| Expected Result | The application provides the expected confirmation or feedback that the product was added to the cart. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-PROD-010 — Navigate back from product details

| Field | Details |
|---|---|
| Feature | Product Details / Navigation |
| Priority | Medium |
| Preconditions | Product detail page is open |
| Test Data | Any available product |
| Steps | 1. Open a product detail page. 2. Use the available navigation or browser Back control. |
| Expected Result | The user returns to the expected product listing or previous page without an application error. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-PROD-011 — Refresh a product detail page

| Field | Details |
|---|---|
| Feature | Product Details |
| Priority | Medium |
| Preconditions | Product detail page is open |
| Test Data | Any available product |
| Steps | 1. Open a product detail page. 2. Refresh the browser. |
| Expected Result | The product detail page reloads successfully and the expected product information remains available. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-PROD-012 — Verify product details remain usable after category navigation

| Field | Details |
|---|---|
| Feature | Product Details / Categories |
| Priority | Medium |
| Preconditions | Product categories are available |
| Test Data | Products from at least two categories |
| Steps | 1. Select a category. 2. Open a product. 3. Return to the product listing. 4. Select another category. 5. Open a product from the second category. |
| Expected Result | Product detail pages load correctly for products selected from different categories. |
| Actual Result | Not Run |
| Status | Not Run |

---

# Product Details Coverage Summary

| Feature | Test Cases |
|---|---:|
| Product Details | 12 |
| Previous Cases | 27 |
| **Total Cases** | **39** |
