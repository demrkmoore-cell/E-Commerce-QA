import os

import requests


BASE_URL = "https://api.demoblaze.com"


def test_add_product_to_cart():
    username = os.getenv("DEMOBLAZE_USERNAME")
    password = os.getenv("DEMOBLAZE_PASSWORD")

    assert username, "DEMOBLAZE_USERNAME is not set"
    assert password, "DEMOBLAZE_PASSWORD is not set"

    login_response = requests.post(
        f"{BASE_URL}/login",
        json={
            "username": username,
            "password": password,
        },
        timeout=10,
    )

    assert login_response.status_code == 200

    token = login_response.json()
    assert token.startswith("Auth_token:")

    auth_token = token.replace("Auth_token:", "").strip()
    assert auth_token

    add_response = requests.post(
        f"{BASE_URL}/addtocart",
        json={
            "id": "python-test-cart-item",
            "cookie": auth_token,
            "prod_id": 1,
            "flag": True,
        },
        timeout=10,
    )

    assert add_response.status_code == 200
