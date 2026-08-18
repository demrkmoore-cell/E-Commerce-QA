from api_client import credentials


def test_login_wrong_password_returns_error(api_client):
    username, _ = credentials()

    response = api_client.login(username, "definitely_wrong_password")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert data.get("errorMessage") == "Wrong password."
