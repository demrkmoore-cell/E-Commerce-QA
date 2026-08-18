# E-Commerce QA Portfolio

End-to-end QA portfolio project for the public Demoblaze e-commerce application. The project demonstrates a practical QA workflow from test planning and manual execution through Jira defect reporting, regression testing, API validation, Python API automation, GitHub Actions CI, SQL/backend validation planning, and UI automation planning.

## Project Overview

**Application:** Demoblaze Product Store  
**API:** `https://api.demoblaze.com`  
**Test environment:** Desktop Chrome / Postman / Python API automation  
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
- Response/status-code validation
- Defect reporting and evidence management in Jira
- SQL/backend validation planning
- UI automation roadmap

## Execution Results

| Result | Count |
|---|---:|
| ✅ Passed | **92** |
| ❌ Failed | **13** |
| ⚠️ Blocked | **1** |
| **Total Executions** | **106** |

The detailed manual execution record is maintained in [`test-summary/execution-results.md`](test-summary/execution-results.md).

## API Testing

API testing was executed against the public Demoblaze API using Postman and Python automation. The collection and automated suite cover authentication, product/catalog operations, shopping-cart operations, and negative scenarios.

### Postman API testing

API techniques demonstrated:

- Positive and negative testing
- Boundary and invalid-input testing
- Request-body manipulation
- Authentication/token validation
- HTTP status-code validation
- Response-body and error-message assertions
- Postman test scripting
- Reproducible defect evidence

The working Postman collection is stored at [`api-tests/Demoblaze-API-Tests.postman_collection.json`](api-tests/Demoblaze-API-Tests.postman_collection.json).

### Python API automation

The repository also contains a Python/Pytest API automation suite in [`python-api-tests/`](python-api-tests/).

The current automated regression suite contains **6 passing tests** covering:

| Automated Test | Endpoint | Coverage |
|---|---|---|
| Login success | `POST /login` | Validates successful authentication and token response |
| Login negative | `POST /login` | Validates invalid-password error handling |
| Product retrieval | `GET /entries` | Validates product collection and required fields |
| Add to cart | `POST /addtocart` | Authenticates and adds a test product |
| View cart | `POST /viewcart` | Verifies the added product appears in the cart |
| Delete cart item | `POST /deleteitem` | Removes the test item and verifies removal |

Technology used:

- Python 3.11
- Pytest
- Requests
- Environment-based credentials
- JSON response validation
- HTTP status-code assertions

Run the suite locally from the repository root with:

```bash
cd python-api-tests
source .venv/bin/activate
pytest -v
```

Expected result for the current suite: **6 passed**.

### GitHub Actions CI

The Python API suite runs automatically through GitHub Actions on pushes and pull requests to `main`, and can also be triggered manually.

Workflow: [`.github/workflows/python-api-tests.yml`](.github/workflows/python-api-tests.yml)

The CI workflow:

1. Checks out the repository
2. Sets up Python 3.11
3. Installs the pinned dependencies from `python-api-tests/requirements.txt`
4. Loads Demoblaze credentials from GitHub Actions Secrets
5. Executes the Pytest API suite
6. Reports the pass/fail result in GitHub Actions

The current CI validation completed successfully with **6/6 API tests passing**.

> Authentication credentials are stored as GitHub Actions Secrets and are not committed to the repository. The repository does not publish passwords, authentication tokens, or other secrets.

## Confirmed API Defect

**EQAP-10 — `/addtocart` returns HTTP 500 when request ID is null**

The test reproduced a server-side HTTP 500 response for invalid client input. Postman assertions passed for the observed behavior, and the Jira defect includes request/response screenshots and reproduction details.

See [`bug-reports/EQAP-10.md`](bug-reports/EQAP-10.md) and [Jira EQAP-10](https://demrkmoore.atlassian.net/browse/EQAP-10).

> The repository does not publish authentication tokens, passwords, or other secrets. Screenshots containing sensitive values should remain attached to Jira or be redacted before public publication.

## Key Manual Testing Findings

The manual execution identified defects involving:

- Login/authentication behavior after registration
- Blank total on an empty shopping cart
- Weak credit-card input validation
- Invalid expiration-month acceptance
- Invalid/expired expiration-year acceptance
- Checkout initiation from an empty cart

Jira defects are tracked under **EQAP-3 through EQAP-8**.

**EQAP-9** is retained as an investigation item because the original cart-loss scenario was observed once but did not reproduce during follow-up testing. Later executions successfully handled multiple products across categories. This project therefore does not present EQAP-9 as a consistently reproducible defect.

## Test Suite vs. Execution Results

This repository intentionally separates **planned test cases** from **executed results**.

### Planned test suite

[`test-cases/functional-test-cases.md`](test-cases/functional-test-cases.md)

This file contains the broader functional test inventory and is the planned test suite. Cases that have not been explicitly mapped to an execution remain marked as **Not Run**.

### Executed results

[`test-summary/execution-results.md`](test-summary/execution-results.md)

This file records the actual manual execution results from the project session, including observed behavior and defect classifications.

This separation prevents the portfolio from claiming that every planned case was executed when the execution evidence does not support that claim.

## Regression Testing

A focused regression strategy is documented in [`regression/README.md`](regression/README.md).

Priority is given to high-risk flows such as:

1. Login/authentication
2. Product/category navigation
3. Add-to-cart and cart calculations
4. Product removal and duplicate handling
5. Checkout validation
6. Empty-cart behavior
7. Cart persistence across refresh/navigation

## Jira Defects

| Jira | Summary | Classification |
|---|---|---|
| EQAP-3 | Registered user cannot log in after successful registration | Confirmed defect |
| EQAP-4 | Empty cart displays a blank total | Confirmed defect |
| EQAP-5 | Checkout accepts invalid credit-card input | Confirmed defect |
| EQAP-6 | Checkout accepts invalid expiration month | Confirmed defect |
| EQAP-7 | Checkout accepts invalid/expired expiration year | Confirmed defect |
| EQAP-8 | Checkout can be initiated with an empty cart | Confirmed defect |
| EQAP-9 | Original multi-category cart-loss observation | Non-reproducible / investigation |
| EQAP-10 | `/addtocart` returns HTTP 500 when request ID is null | Confirmed API defect |

## Evidence

Jira is used as the primary evidence location for defects and their request/response screenshots. Public repository documentation references the evidence without exposing credentials or sensitive payment data.

Recommended naming convention for future redacted evidence:

`TC-<AREA>-<ID>-<condition>-<result>.png`

Payment-related screenshots must be redacted before being uploaded to Jira or committed to a public GitHub repository. Full card numbers and authentication tokens should never be published.

## Repository Structure

```text
E-Commerce-QA/
├── README.md
├── api-tests/
│   ├── Demoblaze-API-Tests.postman_collection.json
│   └── README.md
├── python-api-tests/
│   ├── README.md
│   ├── requirements.txt
│   └── tests/
│       ├── test_authentication.py
│       ├── test_authentication_negative.py
│       ├── test_cart.py
│       ├── test_delete_item.py
│       ├── test_products.py
│       └── test_view_cart.py
├── .github/
│   └── workflows/
│       └── python-api-tests.yml
├── bug-reports/
│   ├── README.md
│   ├── EQAP-3.md ... EQAP-9.md
│   └── EQAP-10.md
├── regression/
│   └── README.md
├── test-cases/
│   └── functional-test-cases.md
├── test-plan/
│   └── QA-Test-Plan.md
└── test-summary/
    └── execution-results.md
```

## Tools & Technologies

- **Jira** — defect tracking and test execution evidence
- **Git / GitHub** — source control, CI, and portfolio presentation
- **GitHub Actions** — continuous integration for automated API tests
- **Postman** — API testing and automated response assertions
- **Python / Pytest** — API test automation
- **Requests** — HTTP/API automation
- **Chrome DevTools** — browser-level investigation
- **SQL / PostgreSQL** — backend validation planning
- **Playwright / Selenium** — UI automation roadmap
- **Markdown** — test documentation

## Automation Strategy

The project does not attempt to automate every manual test. The automation strategy prioritizes high-frequency, high-risk regression flows and demonstrates both API-level automation and CI execution.

### Current automation coverage

- Login smoke coverage
- Invalid-password authentication coverage
- Product/catalog response validation
- Add-to-cart flow
- View-cart verification
- Delete-item flow
- Automated regression execution through GitHub Actions

### Future automation roadmap

The broader automation roadmap prioritizes:

- Category navigation
- Product detail validation
- Cart total calculations
- Core checkout validation
- Additional negative and boundary API scenarios

## SQL / Backend Validation

Backend validation plans focus on verifying stored values and calculated totals without modifying or truncating application data.

## Project Outcome

This project demonstrates the ability to:

- design a structured functional test suite
- execute risk-based manual tests
- perform boundary and negative testing
- validate REST APIs with Postman
- build Python API automation with Pytest and Requests
- integrate automated tests into GitHub Actions CI
- manage test credentials securely with GitHub Actions Secrets
- write automated response assertions
- identify and document defects in Jira
- preserve reproducible request/response evidence
- retest defects and distinguish reproducible issues from non-reproducible behavior
- build a focused regression strategy
- plan SQL and UI automation coverage
- organize QA evidence for a professional portfolio

## Author

**DeMarko Moore**  
QA Engineer | Python | SQL | API Testing | Test Automation | Jira | GitHub
