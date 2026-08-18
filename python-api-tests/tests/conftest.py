import pytest

from api_client import DemoblazeAPIClient, credentials, extract_auth_token


@pytest.fixture
def api_client() -> DemoblazeAPIClient:
    return DemoblazeAPIClient()


@pytest.fixture
def auth_token(api_client: DemoblazeAPIClient) -> str:
    username, password = credentials()
    response = api_client.login(username, password)
    assert response.status_code == 200
    return extract_auth_token(response)
