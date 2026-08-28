# E-Commerce QA Portfolio

[![Python API Tests](https://github.com/demrkmoore-cell/E-Commerce-QA/actions/workflows/python-api-tests.yml/badge.svg)](https://github.com/demrkmoore-cell/E-Commerce-QA/actions/workflows/python-api-tests.yml)

End-to-end QA portfolio project for the public Demoblaze e-commerce application. Demonstrates structured test planning, manual testing, Jira defect reporting, REST API testing, Python API automation, GitHub Actions CI, SQL/backend validation planning, and browser UI automation with Playwright.

## Portfolio at a Glance

| Area | Deliverable | Status |
|---|---|---|
| Test planning | QA test plan and functional test inventory | ✅ Complete |
| Manual testing | 106 recorded executions | ✅ Complete |
| Defect management | Jira defects EQAP-3 through EQAP-10 | ✅ Complete |
| API testing | Postman collection and negative testing | ✅ Complete |
| API automation | 7-test Python/Pytest suite | ✅ Complete |
| CI/CD | GitHub Actions with HTML reporting | ✅ Complete |
| Regression | Focused high-risk regression strategy | ✅ Complete |
| SQL/backend | Validation planning | ✅ Documented |
| UI automation | 3-test Playwright/Pytest suite | ✅ Complete |

## Quick Navigation

- [QA Test Plan](test-plan/QA-Test-Plan.md)
- [Functional Test Cases](test-cases/functional-test-cases.md)
- [Execution Results](test-summary/execution-results.md)
- [Regression Strategy](regression/README.md)
- [Postman API Collection](api-tests/Demoblaze-API-Tests.postman_collection.json)
- [Python API Automation](python-api-tests/README.md)
- [Playwright UI Automation](ui-tests/README.md)
- [Jira Defect Reports](bug-reports/README.md)
- [GitHub Actions Workflow](.github/workflows/python-api-tests.yml)

## Project Overview

**Application:** Demoblaze Product Store  
**API:** `https://api.demoblaze.com`  
**UI:** `https://www.demoblaze.com/`  
**Jira project:** EQAP  
**Repository:** `demrkmoore-cell/E-Commerce-QA`

### QA Scope

- Functional testing
- Regression testing
- Negative and boundary testing
- Product and category validation
- Shopping cart validation
- Checkout validation
- Browser refresh and navigation testing
- REST API testing with Postman
- Python API automation with Pytest and Requests
- GitHub Actions continuous integration
- HTML automated test reporting
- Response/status-code validation
- Defect reporting and evidence management in Jira
- SQL/backend validation planning
- UI automation with Playwright and Chromium

## Execution Results

| Result | Count |
|---|---:|
| ✅ Passed | **92** |
| ❌ Failed | **13** |
| ⚠️ Blocked | **1** |
| **Total Executions** | **106** |

The detailed manual execution record is maintained in [`test-summary/execution-results.md`](test-summary/execution-results.md).

## API Testing

API testing was executed against the public Demoblaze API using Postman and Python automation. Coverage includes authentication, product/catalog operations, shopping-cart operations, and negative scenarios.

### Postman

The working collection is stored at [`api-tests/Demoblaze-API-Tests.postman_collection.json`](api-tests/Demoblaze-API-Tests.postman_collection.json).

Techniques demonstrated include positive/negative testing, boundary and invalid-input testing, authentication/token validation, HTTP status assertions, response-body assertions, Postman test scripting, and reproducible defect evidence.

### Python API automation

The maintainable Python/Pytest suite is documented in [`python-api-tests/README.md`](python-api-tests/README.md). It contains **7 automated tests** using a reusable API client, fixtures, environment-based credentials, JSON validation, HTTP assertions, and GitHub Actions CI. fileciteturn17file0L2-L2

## UI Automation — Playwright

A focused browser automation suite is now included in [`ui-tests/`](ui-tests/).

### Current UI coverage

| Test | Coverage |
|---|---|
| Homepage | Page load, title validation, dynamic product visibility |
| Product selection | Product selection and product-details validation |
| Add to cart | End-to-end product selection, cart addition, and cart verification |

The suite uses **Python, Pytest, Playwright, Chromium, and the Page Object Model**. The local suite completed with **3 passing tests**.

The UI automation is intentionally focused on high-value regression flows rather than attempting to automate the entire manual test inventory.

See [`ui-tests/README.md`](ui-tests/README.md) for setup, project structure, and execution instructions.

## Confirmed API Defect

**EQAP-10 — `/addtocart` returns HTTP 500 when request ID is null**

The test reproduced a server-side HTTP 500 response for invalid client input. The Jira defect includes reproduction details and evidence, while the Python API suite monitors the behavior through regression automation.

See [`bug-reports/EQAP-10.md`](bug-reports/EQAP-10.md) and [Jira EQAP-10](https://demrkmoore.atlassian.net/browse/EQAP-10).

> The repository does not publish authentication tokens, passwords, or other secrets. Screenshots containing sensitive values should remain attached to Jira or be redacted before public publication.

## Key Manual Testing Findings

The manual execution identified defects involving login/authentication behavior, empty-cart totals, weak credit-card validation, invalid expiration-month acceptance, invalid/expired expiration-year acceptance, and checkout initiation from an empty cart.

Jira defects are tracked under **EQAP-3 through EQAP-8**. **EQAP-9** is retained as a non-reproducible investigation item rather than being presented as a confirmed defect.

## Regression Strategy

The focused regression strategy prioritizes:

1. Login/authentication
2. Product/category navigation
3. Add-to-cart and cart calculations
4. Product removal and duplicate handling
5. Checkout validation
6. Empty-cart behavior
7. Cart persistence across refresh/navigation
8. API authentication and shopping-cart regression
9. High-value browser UI flows

See [`regression/README.md`](regression/README.md).

## Repository Structure

```text
E-Commerce-QA/
├── README.md
├── api-tests/
│   ├── Demoblaze-API-Tests.postman_collection.json
│   └── README.md
├── python-api-tests/
│   ├── README.md
│   ├── api_client.py
│   ├── pytest.ini
│   ├── requirements.txt
│   └── tests/
├── ui-tests/
│   ├── README.md
│   ├── pytest.ini
│   ├── requirements.txt
│   ├── pages/
│   │   ├── __init__.py
│   │   ├── home_page.py
│   │   ├── product_page.py
│   │   └── cart_page.py
│   └── tests/
│       ├── test_homepage.py
│       ├── test_product_selection.py
│       └── test_add_to_cart.py
├── .github/
│   └── workflows/
│       └── python-api-tests.yml
├── bug-reports/
├── regression/
├── test-cases/
├── test-plan/
└── test-summary/
```

## Tools & Technologies

- **Jira** — defect tracking and test evidence
- **Git / GitHub** — source control and portfolio presentation
- **GitHub Actions** — continuous integration and reporting
- **Postman** — API testing and response assertions
- **Python / Pytest** — API and UI test automation
- **Requests** — HTTP/API automation
- **Playwright / Chromium** — browser UI automation
- **Page Object Model** — reusable UI test architecture
- **Chrome DevTools** — browser-level investigation
- **SQL / PostgreSQL** — backend validation planning
- **Markdown** — QA documentation

## Project Outcome

This project demonstrates the ability to design structured test suites, execute risk-based manual tests, perform negative and boundary testing, validate REST APIs, build maintainable Python automation, automate browser workflows with Playwright, use reusable test abstractions, integrate automation into CI, document defects in Jira, and organize QA evidence for a professional portfolio.

## Author

**DeMarko Moore**  
QA Engineer | Python | SQL | API Testing | UI Automation | Test Automation | Jira | GitHub
