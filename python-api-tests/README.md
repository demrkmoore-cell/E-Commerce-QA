# Demoblaze Python API Automation

Python API automation suite for the E-Commerce QA Portfolio project.

## Technology

- Python 3.11
- Pytest
- Requests
- Demoblaze REST API

## API Under Test

`https://api.demoblaze.com`

## Automated Coverage

| Test | Endpoint | Coverage |
|---|---|---|
| Authentication | POST /login | Validates successful authentication and token response |
| Products | GET /entries | Validates product collection and required fields |
| Add to Cart | POST /addtocart | Authenticates and adds product ID 1 |
| View Cart | POST /viewcart | Validates cart contents after adding a product |
| Delete Item | POST /deleteitem | Deletes the test item and verifies removal |

## Test Workflow

Login → Add Product → View Cart → Delete Product → Verify Removal

## Setup

Create and activate a virtual environment:

python3 -m venv .venv
source .venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Configure credentials through environment variables:

export DEMOBLAZE_USERNAME="your_username"
export DEMOBLAZE_PASSWORD="your_password"

Do not commit real credentials, authentication tokens, or .env files.

## Run Tests

pytest -v

Expected result for the current suite: 5 passed.

## Portfolio Value

- API functional testing
- Authentication handling
- Environment-based credentials
- HTTP status validation
- JSON response validation
- Dynamic test data handling
- End-to-end API workflows
- Automated regression coverage
- Pytest test organization

## Related Portfolio Work

- Postman API collection
- Functional test cases
- Jira defect reports
- Test execution results
- QA test plan
- SQL/backend validation planning
