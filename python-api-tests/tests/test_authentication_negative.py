import os

import requests


BASE_URL = "https://api.demoblaze.com"


def test_login_wrong_password_returns_error():
    username = os.getenv("DEMOBLAZE_USERNAME")
    password = os.getenv("DEMOBLAZE_PASSWORD")

    assert username, "DEMOBLAZE_USERNAME is not set"
    assert password, "DEMOBLAZE_PASSWORD is not set"

    response = requests.post(
        f"{BASE_URL}/login",
        json={
            "username": username,
            "password": "definitely_wrong_password",
        },
        timeout=10,
    )

    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, dict)
    assert data.get("errorMessage") == "Wrong password."
