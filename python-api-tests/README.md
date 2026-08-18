# Demoblaze Python API Automation

Python API automation suite for the E-Commerce QA Portfolio project.

## Purpose

This suite demonstrates maintainable API automation using **Python, Pytest, Requests, fixtures, reusable API-client methods, environment-based credentials, and GitHub Actions CI**.

## Technology

- Python 3.11
- Pytest
- Requests
- pytest-html
- GitHub Actions
- Demoblaze REST API

## API Under Test

`https://api.demoblaze.com`

## Automated Coverage

| Test | Endpoint | Coverage |
|---|---|---|
| Authentication | `POST /login` | Validates successful authentication and token response |
| Authentication negative | `POST /login` | Validates invalid-password error handling |
| Products | `GET /entries` | Validates product collection and required fields |
| Add to Cart | `POST /addtocart` | Authenticates and adds a test product |
| View Cart | `POST /viewcart` | Verifies the added product appears in the cart |
| Delete Item | `POST /deleteitem` | Deletes the test item and verifies removal |

**Current suite: 6 automated tests.**

## Framework Design

The suite uses a small reusable API client in [`api_client.py`](api_client.py) and shared Pytest fixtures in [`tests/conftest.py`](tests/conftest.py).

- `DemoblazeAPIClient` centralizes HTTP requests and endpoint payloads.
- `auth_token` provides authenticated tests with a reusable login fixture.
- Credentials are read from environment variables instead of source code.
- Each test focuses on behavior and assertions rather than repeated setup code.

## Test Workflow

`Login → Add Product → View Cart → Delete Product → Verify Removal`

## Setup

From the repository root:

```bash
cd python-api-tests
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Configure credentials through environment variables:

```bash
export DEMOBLAZE_USERNAME="your_username"
export DEMOBLAZE_PASSWORD="your_password"
```

Do not commit real credentials, authentication tokens, or `.env` files.

## Run Tests

Run the suite with:

```bash
pytest -v
```

Generate a local HTML report:

```bash
pytest -v --html=reports/api-test-report.html --self-contained-html
```

The CI workflow generates the same report and uploads it as a GitHub Actions artifact.

## Continuous Integration

The workflow at [`../.github/workflows/python-api-tests.yml`](../.github/workflows/python-api-tests.yml) runs on pushes and pull requests to `main`, and supports manual execution.

CI performs the following steps:

1. Checks out the repository.
2. Installs Python 3.11 and pinned dependencies.
3. Loads credentials from GitHub Actions Secrets.
4. Runs all API tests.
5. Generates a self-contained HTML test report.
6. Uploads the report as a workflow artifact even when tests fail.

## Portfolio Value

- API functional testing
- Positive and negative testing
- Authentication handling
- Environment-based credentials
- Reusable API-client design
- Pytest fixtures
- HTTP status validation
- JSON response validation
- Dynamic test data handling
- End-to-end API workflows
- Automated regression coverage
- HTML test reporting
- GitHub Actions CI

## Related Portfolio Work

- Postman API collection
- Functional test cases
- Jira defect reports
- Test execution results
- QA test plan
- Regression strategy
- SQL/backend validation planning
