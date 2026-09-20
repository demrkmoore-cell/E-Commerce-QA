import time

import pytest

from api_client import DemoblazeAPIClient, extract_auth_token


@pytest.fixture
def api_client() -> DemoblazeAPIClient:
    return DemoblazeAPIClient()


@pytest.fixture
def test_credentials() -> tuple[str, str]:
    unique_id = int(time.time() * 1000)
    return f"qa_api_{unique_id}", f"TestPass_{unique_id}_X"


@pytest.fixture
def auth_token(
    api_client: DemoblazeAPIClient,
    test_credentials: tuple[str, str],
) -> str:
    username, password = test_credentials

    signup_response = api_client.signup(username, password)
    assert signup_response.status_code == 200

    login_response = api_client.login(username, password)
    assert login_response.status_code == 200

    return extract_auth_token(login_response)
