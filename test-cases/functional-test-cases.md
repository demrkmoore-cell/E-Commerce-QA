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

# Initial Coverage Summary

| Feature | Test Cases |
|---|---:|
| Registration | 8 |
| Login / Logout | 7 |
| **Total** | **15** |

## Execution Notes

These cases are currently **Not Run**. Actual results will be recorded after execution against the Demoblaze application.

Additional functional coverage will be added for:

- Navigation and Categories
- Product Details
- Shopping Cart
- Checkout and Orders
- Negative and Boundary Scenarios
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

## Execution Notes

These Navigation & Categories cases are currently **Not Run**. Actual results will be recorded during test execution against the Demoblaze application.

Next planned coverage:

- Product Details
- Shopping Cart
- Checkout & Orders
- Negative & Boundary Scenarios
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

## Execution Notes

Product Details cases are currently **Not Run**. Actual results will be recorded during execution against the Demoblaze application.

Next planned coverage:

- Shopping Cart
- Checkout & Orders
- Negative & Boundary Scenarios
---

# Product Details Coverage Summary

| Feature | Test Cases |
|---|---:|
| Product Details | 12 |
| Previous Cases | 27 |
| **Total Cases** | **39** |


---

# 5. Shopping Cart

## TC-CART-001 — Open the shopping cart

| Field | Details |
|---|---|
| Feature | Shopping Cart |
| Priority | High |
| Preconditions | Demoblaze home page is accessible |
| Test Data | None |
| Steps | 1. Open Demoblaze. 2. Select Cart. |
| Expected Result | The Shopping Cart page opens successfully. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-CART-002 — Verify empty cart state

| Field | Details |
|---|---|
| Feature | Shopping Cart |
| Priority | High |
| Preconditions | No products have been added to the cart |
| Test Data | Empty cart |
| Steps | 1. Open the Shopping Cart. |
| Expected Result | The cart loads and does not display products that were not added by the user. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-CART-003 — Add one product to the cart

| Field | Details |
|---|---|
| Feature | Shopping Cart |
| Priority | Critical |
| Preconditions | Home page is loaded |
| Test Data | One available product |
| Steps | 1. Open a product. 2. Select Add to cart. 3. Open Cart. |
| Expected Result | The selected product appears in the cart. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-CART-004 — Verify product name in cart

| Field | Details |
|---|---|
| Feature | Shopping Cart |
| Priority | High |
| Preconditions | One product has been added to the cart |
| Test Data | Any available product |
| Steps | 1. Add a product to the cart. 2. Open Cart. 3. Compare the product name with the product that was selected. |
| Expected Result | The cart displays the correct product name. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-CART-005 — Verify product price in cart

| Field | Details |
|---|---|
| Feature | Shopping Cart |
| Priority | Critical |
| Preconditions | One product has been added |
| Test Data | Any available product |
| Steps | 1. Record the product price from the product page. 2. Add the product to the cart. 3. Open Cart. 4. Compare the displayed price. |
| Expected Result | The cart displays the correct price for the selected product. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-CART-006 — Verify cart total for one product

| Field | Details |
|---|---|
| Feature | Shopping Cart |
| Priority | Critical |
| Preconditions | One product is in the cart |
| Test Data | One available product |
| Steps | 1. Add one product. 2. Open Cart. 3. Compare the displayed total with the product price. |
| Expected Result | The cart total correctly reflects the product price. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-CART-007 — Add multiple different products

| Field | Details |
|---|---|
| Feature | Shopping Cart |
| Priority | Critical |
| Preconditions | Home page is available |
| Test Data | Two or more different products |
| Steps | 1. Add the first product to the cart. 2. Return to the product listing. 3. Add a second product. 4. Open Cart. |
| Expected Result | All selected products appear in the cart. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-CART-008 — Verify total for multiple products

| Field | Details |
|---|---|
| Feature | Shopping Cart |
| Priority | Critical |
| Preconditions | Multiple products are in the cart |
| Test Data | Two or more products with known prices |
| Steps | 1. Add multiple products. 2. Open Cart. 3. Calculate the expected total from the displayed product prices. 4. Compare it with the cart total. |
| Expected Result | The displayed cart total equals the sum of the applicable product prices. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-CART-009 — Remove a product from the cart

| Field | Details |
|---|---|
| Feature | Shopping Cart |
| Priority | Critical |
| Preconditions | At least one product is in the cart |
| Test Data | One or more products |
| Steps | 1. Open Cart. 2. Select Delete for a product. |
| Expected Result | The selected product is removed from the cart and the cart information is updated. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-CART-010 — Remove one product while retaining another

| Field | Details |
|---|---|
| Feature | Shopping Cart |
| Priority | High |
| Preconditions | At least two different products are in the cart |
| Test Data | Product A and Product B |
| Steps | 1. Add Product A. 2. Add Product B. 3. Open Cart. 4. Remove Product A. |
| Expected Result | Product A is removed while Product B remains in the cart. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-CART-011 — Verify cart total updates after product removal

| Field | Details |
|---|---|
| Feature | Shopping Cart |
| Priority | Critical |
| Preconditions | Multiple products are in the cart |
| Test Data | Two or more products |
| Steps | 1. Record the initial cart total. 2. Remove one product. 3. Observe the updated total. |
| Expected Result | The cart total is recalculated to reflect the remaining products. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-CART-012 — Navigate from cart back to products

| Field | Details |
|---|---|
| Feature | Shopping Cart / Navigation |
| Priority | Medium |
| Preconditions | Cart page is open |
| Test Data | None |
| Steps | 1. Open Cart. 2. Navigate back to the product listing/home page. |
| Expected Result | The user can return to the product browsing experience without an application error. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-CART-013 — Add a product after returning from the cart

| Field | Details |
|---|---|
| Feature | Shopping Cart |
| Priority | High |
| Preconditions | Cart can be opened successfully |
| Test Data | Two different products |
| Steps | 1. Add Product A. 2. Open Cart. 3. Return to products. 4. Add Product B. 5. Open Cart again. |
| Expected Result | Both selected products are represented correctly in the cart. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-CART-014 — Refresh the cart page

| Field | Details |
|---|---|
| Feature | Shopping Cart |
| Priority | Medium |
| Preconditions | Product(s) are present in the cart |
| Test Data | One or more products |
| Steps | 1. Open Cart. 2. Refresh the browser page. |
| Expected Result | The cart reloads without an application error and the resulting cart state is consistent with the application's implemented behavior. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-CART-015 — Proceed from cart to checkout

| Field | Details |
|---|---|
| Feature | Shopping Cart / Checkout |
| Priority | Critical |
| Preconditions | At least one product is in the cart |
| Test Data | One available product |
| Steps | 1. Add a product to the cart. 2. Open Cart. 3. Select the checkout/order control. |
| Expected Result | The checkout/order interface opens successfully and presents the expected fields or controls required to complete the order. |
| Actual Result | Not Run |
| Status | Not Run |

---

# Shopping Cart Coverage Summary

| Feature | Test Cases |
|---|---:|
| Shopping Cart | 15 |
| Previous Cases | 39 |
| **Total Cases** | **54** |

## Execution Notes

Shopping Cart cases are currently **Not Run**. Actual results will be recorded during execution against the Demoblaze application.

Next planned coverage:

- Checkout & Orders
- Negative & Boundary Scenarios
- Final regression suite selection

- ---

# 6. Checkout & Orders

## TC-CHECKOUT-001 — Open checkout from the shopping cart

| Field | Details |
|---|---|
| Feature | Checkout |
| Priority | Critical |
| Preconditions | At least one product is in the cart |
| Test Data | One available product |
| Steps | 1. Add a product to the cart. 2. Open the Shopping Cart. 3. Select the checkout/order control. |
| Expected Result | The checkout/order dialog opens successfully. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-CHECKOUT-002 — Verify checkout form fields are displayed

| Field | Details |
|---|---|
| Feature | Checkout |
| Priority | Critical |
| Preconditions | Checkout/order dialog is open |
| Test Data | None |
| Steps | 1. Open checkout. 2. Review the available form fields. |
| Expected Result | The expected customer and payment/order fields are displayed and available for input. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-CHECKOUT-003 — Complete checkout with valid information

| Field | Details |
|---|---|
| Feature | Checkout |
| Priority | Critical |
| Preconditions | At least one product is in the cart and checkout is available |
| Test Data | Valid test customer information and valid non-sensitive test payment information appropriate for the demo environment |
| Steps | 1. Add a product to the cart. 2. Open checkout. 3. Enter valid information into the required fields. 4. Submit/place the order. |
| Expected Result | The application accepts the valid information and processes the order according to the application's implemented behavior. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-CHECKOUT-004 — Submit checkout with an empty name field

| Field | Details |
|---|---|
| Feature | Checkout Validation |
| Priority | High |
| Preconditions | Checkout/order dialog is open |
| Test Data | Name: blank; remaining fields populated with valid test data |
| Steps | 1. Leave the name field empty. 2. Complete the remaining fields. 3. Attempt to place the order. |
| Expected Result | The application handles the missing required name according to its implemented validation behavior and does not incorrectly accept incomplete information. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-CHECKOUT-005 — Submit checkout with an empty country field

| Field | Details |
|---|---|
| Feature | Checkout Validation |
| Priority | High |
| Preconditions | Checkout/order dialog is open |
| Test Data | Country: blank; remaining fields populated with valid test data |
| Steps | 1. Leave the country field empty. 2. Complete the remaining fields. 3. Attempt to place the order. |
| Expected Result | The application handles the missing country according to its implemented validation behavior. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-CHECKOUT-006 — Submit checkout with an empty city field

| Field | Details |
|---|---|
| Feature | Checkout Validation |
| Priority | High |
| Preconditions | Checkout/order dialog is open |
| Test Data | City: blank; remaining fields populated with valid test data |
| Steps | 1. Leave the city field empty. 2. Complete the remaining fields. 3. Attempt to place the order. |
| Expected Result | The application handles the missing city according to its implemented validation behavior. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-CHECKOUT-007 — Submit checkout with an empty credit card field

| Field | Details |
|---|---|
| Feature | Checkout Validation |
| Priority | Critical |
| Preconditions | Checkout/order dialog is open |
| Test Data | Credit card: blank; remaining fields populated with valid test data |
| Steps | 1. Leave the credit card field empty. 2. Complete the remaining fields. 3. Attempt to place the order. |
| Expected Result | The application handles the missing payment information according to its implemented behavior and does not incorrectly accept incomplete payment data. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-CHECKOUT-008 — Submit checkout with an empty month field

| Field | Details |
|---|---|
| Feature | Checkout Validation |
| Priority | High |
| Preconditions | Checkout/order dialog is open |
| Test Data | Month: blank; remaining fields populated with valid test data |
| Steps | 1. Leave the month field empty. 2. Complete the remaining fields. 3. Attempt to place the order. |
| Expected Result | The application handles the missing month according to its implemented validation behavior. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-CHECKOUT-009 — Submit checkout with an empty year field

| Field | Details |
|---|---|
| Feature | Checkout Validation |
| Priority | High |
| Preconditions | Checkout/order dialog is open |
| Test Data | Year: blank; remaining fields populated with valid test data |
| Steps | 1. Leave the year field empty. 2. Complete the remaining fields. 3. Attempt to place the order. |
| Expected Result | The application handles the missing year according to its implemented validation behavior. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-CHECKOUT-010 — Verify checkout order total matches cart total

| Field | Details |
|---|---|
| Feature | Checkout / Order Total |
| Priority | Critical |
| Preconditions | Product(s) are in the cart |
| Test Data | One or more products |
| Steps | 1. Record the cart total. 2. Open checkout. 3. Compare the displayed order total with the cart total. |
| Expected Result | The checkout order total is consistent with the applicable cart total. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-CHECKOUT-011 — Complete checkout with multiple products

| Field | Details |
|---|---|
| Feature | Checkout / Orders |
| Priority | Critical |
| Preconditions | Multiple products are in the cart |
| Test Data | Two or more different products |
| Steps | 1. Add multiple products to the cart. 2. Open checkout. 3. Enter valid test information. 4. Submit/place the order. |
| Expected Result | The order is processed according to the application's implemented behavior and reflects the selected products. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-CHECKOUT-012 — Cancel or close the checkout dialog

| Field | Details |
|---|---|
| Feature | Checkout |
| Priority | Medium |
| Preconditions | Checkout/order dialog is open |
| Test Data | None |
| Steps | 1. Open checkout. 2. Select the available Cancel or Close control. |
| Expected Result | The checkout dialog closes without incorrectly submitting an order. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-CHECKOUT-013 — Verify successful order confirmation

| Field | Details |
|---|---|
| Feature | Orders |
| Priority | Critical |
| Preconditions | Valid order information has been submitted |
| Test Data | Valid test checkout information |
| Steps | 1. Complete checkout using valid test information. 2. Submit the order. |
| Expected Result | The application displays an order-success confirmation containing the expected order information. |
| Actual Result | Not Run |
| Status | Not Run |

## TC-CHECKOUT-014 — Verify order completion does not display an application error

| Field | Details |
|---|---|
| Feature | Orders |
| Priority | Critical |
| Preconditions | A valid order is submitted |
| Test Data | Valid test checkout information |
| Steps | 1. Complete a valid checkout. 2. Observe the confirmation/result screen. |
| Expected Result | The order completes without an unexpected application error, broken page, or unhandled exception visible to the user. |
| Actual Result | Not Run |
| Status | Not Run |

---

# Checkout & Orders Coverage Summary

| Feature | Test Cases |
|---|---:|
| Checkout & Orders | 14 |
| Previous Cases | 54 |
| **Total Cases** | **68** |

## Execution Notes

Checkout & Orders cases are currently **Not Run**. Actual results will be recorded during execution against the Demoblaze application.

The next planned section will focus on **Negative & Boundary Scenarios** and will provide additional risk-based coverage beyond the primary customer workflows.
