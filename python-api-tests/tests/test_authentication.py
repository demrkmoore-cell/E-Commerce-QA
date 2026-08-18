from api_client import credentials, extract_auth_token


def test_login_success(api_client):
    username, password = credentials()

    response = api_client.login(username, password)

    assert response.status_code == 200
    token = extract_auth_token(response)
    assert token
