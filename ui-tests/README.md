# Demoblaze UI Automation

A focused Playwright UI automation suite for the public Demoblaze e-commerce application.

## Coverage

The suite currently covers 10 automated scenarios:

### Positive coverage

1. Homepage product visibility
2. Product selection and product-details validation
3. Product detail content validation
4. Add-to-cart workflow and selected product verification

### Negative coverage

5. Nonexistent product ID
6. Malformed product ID
7. Empty product ID
8. Invalid application route returning HTTP 404
9. Product API failure simulation returning HTTP 500 and verifying that product cards are not rendered
10. Cart total validation across product page, cart item, and calculated cart total

The negative scenarios intentionally exercise invalid input, boundary conditions, HTTP error handling, and backend/API failure behavior.

## Technology

- Python 3.11
- Pytest
- Playwright
- Chromium
- Page Object Model (POM)
- Network interception and response validation

## Project Structure

```text
ui-tests/
├── README.md
├── requirements.txt
├── pytest.ini
├── pages/
│   ├── __init__.py
│   ├── home_page.py
│   ├── product_page.py
│   └── cart_page.py
└── tests/
    ├── test_homepage.py
    ├── test_product_selection.py
    ├── test_product_details.py
    ├── test_invalid_product.py
    ├── test_malformed_product.py
    ├── test_empty_product_id.py
    ├── test_invalid_route.py
    ├── test_api_failure.py
    ├── test_add_to_cart.py
    └── test_cart_total.py
```

## Setup (Windows, macOS, or Linux)

Prerequisites: Git and Python 3.11 installed. Open a terminal and clone the repository, then enter the UI test directory:

```bash
git clone https://github.com/demrkmoore-cell/E-Commerce-QA.git
cd E-Commerce-QA/ui-tests
```

Create and activate a virtual environment.

**macOS / Linux / ChromeOS Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows PowerShell:**

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the dependencies and Chromium browser:

```bash
python -m pip install -r requirements.txt
python -m playwright install chromium
```

## Live Browser Demo

With the virtual environment activated and dependencies installed, run this command from the `ui-tests` directory:

```bash
python -m pytest -v --headed --browser chromium
```

The `--headed` option opens a visible Chromium window while the tests run. Expected result: **10 passed**. To run without opening a visible browser, omit `--headed`.

**Display note:** A visible browser requires a desktop session/display. On a headless machine or CI runner, use `python -m pytest -v --browser chromium` instead; CI runs headlessly by design.

## CI Verification

The Playwright suite is also executed by GitHub Actions from the `ui-tests` directory using Python 3.11 and Chromium. CI runs the suite headlessly.

## Latest Local Result

The suite was executed locally against Demoblaze with Chromium and completed with **10 passed** tests.

The automation uses condition-based waits for dynamically rendered content. The API-failure scenario uses Playwright network interception to simulate a server-side failure and validate the resulting UI state.

## QA Value

This UI layer complements the repository's API testing by demonstrating validation at both the API and browser levels. The suite uses reusable Page Objects for core product flows and includes negative testing for invalid product identifiers, malformed input, invalid routes, and simulated backend failure.

The add-to-cart test demonstrates an end-to-end user workflow by selecting a product, adding it to the cart, opening the cart, and verifying that the selected product appears. The network-failure test is particularly useful for demonstrating that UI automation can validate frontend behavior when a dependent backend service returns an error.
