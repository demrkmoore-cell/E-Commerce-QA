from api_client import extract_auth_token


def test_login_success(api_client, test_credentials):
    username, password = test_credentials

    signup_response = api_client.signup(username, password)
    assert signup_response.status_code == 200

    response = api_client.login(username, password)

    assert response.status_code == 200
    token = extract_auth_token(response)
    assert token
