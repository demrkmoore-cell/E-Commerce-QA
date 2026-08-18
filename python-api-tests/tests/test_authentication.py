import os

import requests


BASE_URL = "https://api.demoblaze.com"


def test_login_success():
    username = os.getenv("DEMOBLAZE_USERNAME")
    password = os.getenv("DEMOBLAZE_PASSWORD")

    assert username, "DEMOBLAZE_USERNAME is not set"
    assert password, "DEMOBLAZE_PASSWORD is not set"

    response = requests.post(
        f"{BASE_URL}/login",
        json={
            "username": username,
            "password": password,
        },
        timeout=10,
    )

    assert response.status_code == 200

    token = response.json()
    assert token.startswith("Auth_token:")
    assert token.replace("Auth_token:", "").strip()
