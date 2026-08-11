# E-Commerce QA Test Plan

## 1. Document Information

| Field | Value |
|---|---|
| Project | E-Commerce QA Portfolio |
| Application Under Test | Demoblaze |
| Repository | `demrkmoore-cell/E-Commerce-QA` |
| Jira Project | E-Commerce QA Portfolio (EQAP) |
| Test Approach | Manual, API, UI Automation, Regression, and Data Validation |
| Document Status | Draft / Living Document |
| Owner | DeMarko Moore |

## 2. Purpose

This test plan defines the strategy, scope, objectives, environments, test coverage, data, risks, and completion criteria for quality assurance testing of the Demoblaze public e-commerce application.

The project is designed as an independent QA portfolio project demonstrating an end-to-end testing workflow using Jira and GitHub.

## 3. Test Objectives

- Verify critical customer-facing e-commerce workflows function as expected.
- Validate positive, negative, boundary, and error-handling scenarios.
- Identify, document, prioritize, and track defects through Jira.
- Validate applicable API behavior using request/response testing.
- Build automated UI coverage for stable, high-value workflows.
- Perform regression testing after identified defects or application changes.
- Validate backend/data behavior where publicly accessible data or APIs make meaningful validation possible.
- Produce traceable QA evidence and a final test summary.

## 4. Scope

### 4.1 In Scope

The test effort will cover publicly available Demoblaze functionality that can be exercised without unauthorized access, including:

- Application navigation and page loading
- Product catalog and product details
- Product categories
- Product selection and cart behavior
- Add/remove cart functionality
- Cart totals and displayed product information
- Checkout/order placement workflow
- Required checkout fields and validation
- User-facing error handling
- Navigation and links
- Browser-based UI behavior
- Applicable API endpoints and responses
- Regression coverage for critical workflows
- Defect reporting and retesting
- Automated testing of selected stable workflows

### 4.2 Out of Scope

- Security penetration testing or exploitation
- Load/stress testing against the public application
- Destructive testing that could affect other users or the service
- Access to private administrative functionality without authorization
- Production database access that is not publicly provided
- Testing that violates the application's terms of use

## 5. Test Types

### Functional Testing

Verify that application features meet their expected functional behavior.

### UI Testing

Validate visible controls, navigation, forms, product information, cart behavior, and checkout interactions.

### API Testing

Validate applicable public/API endpoints for status codes, response structure, required fields, data behavior, and negative scenarios.

### Regression Testing

Re-execute critical tests after defects, automation changes, or other relevant application changes.

### Negative Testing

Verify the application handles invalid, missing, unexpected, and boundary input appropriately.

### Boundary and Equivalence Testing

Apply equivalence classes and boundary-value analysis where input rules can be identified.

### Compatibility Testing

Exercise supported workflows in selected browsers and viewport sizes where practical.

### Data Validation

Validate displayed calculations, product information, order information, and API data where sufficient access exists.

### UI Automation

Automate repeatable, high-value workflows using a maintainable test framework and page/object abstractions where appropriate.

## 6. Test Environment

| Area | Planned Configuration |
|---|---|
| Application | Demoblaze public/demo e-commerce application |
| Primary Browser | Chromium/Chrome |
| Secondary Browser | Firefox or another available supported browser |
| Automation Language | Python |
| UI Automation | Selenium or Playwright, based on final framework selection |
| API Tool | Postman and/or Python requests |
| Test Framework | Pytest |
| Version Control | Git/GitHub |
| Defect Tracking | Jira |
| Data Validation | SQL where a legitimate accessible data source exists |

Actual browser and tool versions will be recorded when test execution begins.

## 7. Test Data

Test data will be created specifically for this portfolio project and will not contain real personal, payment, or sensitive information.

Planned data categories include:

- Valid product selections
- Empty cart scenarios
- Multiple-product cart scenarios
- Valid checkout information
- Missing required checkout information
- Invalid input values
- Boundary and unusual input values
- API request payloads
- Expected and actual response data

## 8. Test Execution Strategy

Testing will be performed in the following sequence:

1. Review the application and identify testable functionality.
2. Define requirements and acceptance expectations from observable application behavior.
3. Build the master test plan.
4. Create functional test cases using risk-based prioritization.
5. Execute exploratory and functional tests.
6. Log defects in Jira with reproducible evidence.
7. Build the regression suite around critical workflows.
8. Develop API tests for applicable endpoints.
9. Develop UI automation for stable, high-value scenarios.
10. Perform applicable data/backend validation.
11. Retest resolved defects.
12. Execute regression testing.
13. Document results and publish the final test summary.

## 9. Risk-Based Prioritization

### Priority 1 — Critical

Business-critical workflows whose failure prevents a customer from completing a primary transaction, such as product selection, cart operations, or checkout/order placement.

### Priority 2 — High

Important functionality that significantly affects usability or customer experience, such as navigation, categories, product details, and validation behavior.

### Priority 3 — Medium

Secondary functionality, compatibility scenarios, and lower-risk UI behaviors.

### Priority 4 — Low

Cosmetic or low-impact issues that do not prevent normal use.

## 10. Entry Criteria

Testing can begin when:

- The application is accessible.
- The Jira project is available for tracking.
- The GitHub repository is available for documentation and automation code.
- Initial test scope has been defined.
- Required tools are available.
- Test data can be created safely.

## 11. Exit Criteria

The planned test cycle may be considered complete when:

- Planned high-priority test cases have been executed.
- Critical workflows have been tested successfully or documented with known defects.
- Critical and high-severity defects have been retested where fixes are available.
- Regression testing has been completed for impacted critical functionality.
- API and automation tests included in the agreed scope have been executed.
- Test results and defects are documented.
- Known limitations and residual risks are recorded.
- The final test summary report is completed.

## 12. Defect Management

Defects will be reported in Jira using reproducible information, including:

- Summary
- Environment
- Preconditions
- Steps to reproduce
- Expected result
- Actual result
- Severity
- Priority
- Evidence such as screenshots or logs when useful
- Related test case or requirement
- Retest result

Defects will be tracked through the Jira workflow until resolved, rejected, deferred, or otherwise dispositioned.

## 13. Traceability

The project will maintain traceability between QA work products:

**Requirement / Expected Behavior → Test Case → Execution Result → Defect → Retest → Regression Result**

Jira will provide work-item and defect tracking, while GitHub will contain the detailed QA artifacts and automation implementation.

## 14. Deliverables

The planned project deliverables are:

- QA Test Plan
- Functional test cases
- Regression test suite
- API test collection/scripts
- UI automation suite
- Backend/data validation scripts where applicable
- Jira defect reports
- Test execution results
- Test evidence
- Final test summary report
- Updated project README

## 15. Assumptions and Constraints

- Demoblaze is a public/demo application and may change without notice.
- Public application behavior may differ from a production e-commerce platform.
- Backend/database access may be limited or unavailable.
- API endpoints may change or be unavailable at times.
- Test execution will be performed only within authorized and publicly accessible functionality.
- Test results will record the environment and date of execution to account for application changes.

## 16. Risks and Mitigations

| Risk | Impact | Mitigation |
|---|---|---|
| Public application changes | Test instability | Record execution date and update affected tests |
| Service availability issues | Delayed execution | Document outages and retry during a later test window |
| Limited backend access | Reduced data validation | Validate through available API/UI evidence and document limitation |
| Automation instability | False failures | Use stable selectors, waits, and maintainable page abstractions |
| Environment differences | Inconsistent results | Record browser, version, OS, and execution details |

## 17. Reporting

The final test summary will report:

- Scope completed
- Tests planned and executed
- Pass/fail/blocked results
- Defects by severity and status
- Automation results
- Regression results
- Known limitations
- Residual risks
- Overall QA assessment

## 18. Change History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0 | 2026-08-11 | DeMarko Moore | Initial QA test plan created |
