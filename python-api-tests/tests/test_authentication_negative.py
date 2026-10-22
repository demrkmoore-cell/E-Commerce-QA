def test_login_wrong_password_returns_error(api_client, test_credentials):
    username, _ = test_credentials

    signup_response = api_client.signup(username, "CorrectPass_2026_X")
    assert signup_response.status_code == 200

    response = api_client.login(username, "definitely_wrong_password")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert data.get("errorMessage") == "Wrong password."
