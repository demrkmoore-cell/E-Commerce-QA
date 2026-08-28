# Demoblaze UI Automation

A focused Playwright UI automation suite for the public Demoblaze e-commerce application.

## Coverage

The suite currently covers:

1. Homepage product visibility
2. Product selection and product-details validation
3. End-to-end add-to-cart flow

## Technology

- Python 3.11
- Pytest
- Playwright
- Chromium
- Page Object Model (POM)

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
    └── test_add_to_cart.py
```

## Local Setup

From the `ui-tests` directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m playwright install chromium
pytest -v
```

## Latest Local Result

The suite was executed locally against Demoblaze with Chromium and completed with **3 passed** tests.

The automation intentionally uses condition-based waits for dynamically rendered content instead of fixed sleep intervals.

## QA Value

This UI layer complements the repository's API testing by demonstrating the ability to validate the same e-commerce application at both the API and browser levels. The suite uses reusable Page Objects so locators and UI actions remain separated from test assertions.
