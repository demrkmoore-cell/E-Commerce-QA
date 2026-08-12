# E-Commerce QA Portfolio

End-to-end QA portfolio project for the public Demoblaze e-commerce application. The project demonstrates a practical QA workflow from test planning and manual execution through Jira defect reporting, regression selection, API validation, SQL/backend validation planning, and UI automation planning.

## Project Overview

**Application:** Demoblaze Product Store  
**Test environment:** Desktop Chrome  
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
- Defect reporting and retesting in Jira
- API testing plan
- SQL/backend validation plan
- UI automation roadmap

## Execution Results

| Result | Count |
|---|---:|
| ✅ Passed | **92** |
| ❌ Failed | **13** |
| ⚠️ Blocked | **1** |
| **Total Executions** | **106** |

The detailed execution record is maintained separately in [`test-summary/execution-results.md`](test-summary/execution-results.md).

## Key Findings

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

| Jira | Summary | Current classification |
|---|---|---|
| EQAP-3 | Registered user cannot log in after successful registration | Confirmed defect |
| EQAP-4 | Empty cart displays a blank total | Confirmed defect |
| EQAP-5 | Checkout accepts invalid credit-card input | Confirmed defect |
| EQAP-6 | Checkout accepts invalid expiration month | Confirmed defect |
| EQAP-7 | Checkout accepts invalid/expired expiration year | Confirmed defect |
| EQAP-8 | Checkout can be initiated with an empty cart | Confirmed defect |
| EQAP-9 | Original multi-category cart-loss observation | Non-reproducible / investigation |

## Evidence

Screenshots and other test evidence should be stored in the `evidence/` area using a consistent naming convention such as:

`TC-CHECKOUT-013-invalid-year-0000-accepted.png`

Payment-related screenshots must be redacted before being uploaded to Jira or committed to a public GitHub repository. Full card numbers should never be published.

## Tools & Technologies

- **Jira** — defect tracking and test execution evidence
- **Git / GitHub** — source control and portfolio presentation
- **Chrome DevTools** — browser-level investigation
- **Postman** — API testing
- **SQL / PostgreSQL** — backend validation
- **Python / Pytest** — automation
- **Playwright / Selenium** — UI automation roadmap
- **Markdown** — test documentation

## Automation Strategy

The project does not attempt to automate every manual test. The automation roadmap prioritizes high-frequency, high-risk regression flows such as:

- Login smoke coverage
- Category navigation
- Product detail validation
- Add/remove cart flows
- Cart total calculations
- Core checkout validation

See the [`automation/`](automation/) directory for the planned automation structure.

## API Testing

API testing is planned around the application's available service endpoints, including positive and negative validation of create/delete operations where applicable.

See [`api-tests/`](api-tests/) for the API test documentation.

## SQL / Backend Validation

Backend validation plans focus on verifying stored values and calculated totals without modifying or truncating application data.

See [`sql-validation/`](sql-validation/) for the validation approach.

## Project Outcome

This project demonstrates the ability to:

- design a structured functional test suite
- execute risk-based manual tests
- perform boundary and negative testing
- identify and document defects in Jira
- retest defects and distinguish reproducible issues from non-reproducible behavior
- build a focused regression strategy
- plan API, SQL, and UI automation coverage
- organize QA evidence for a professional portfolio

## Author

**DeMarko Moore**  
QA Engineer | Python | SQL | API Testing | Test Automation | Jira | GitHub
