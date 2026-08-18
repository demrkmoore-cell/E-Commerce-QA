import os
import requests

BASE_URL = "https://api.demoblaze.com"


def test_view_cart_contains_product():
    username = os.getenv("DEMOBLAZE_USERNAME")
    password = os.getenv("DEMOBLAZE_PASSWORD")

    assert username, "DEMOBLAZE_USERNAME is not set"
    assert password, "DEMOBLAZE_PASSWORD is not set"

    login_response = requests.post(
        f"{BASE_URL}/login",
        json={"username": username, "password": password},
        timeout=10,
    )

    assert login_response.status_code == 200

    token = login_response.json()
    assert token.startswith("Auth_token:")
    auth_token = token.replace("Auth_token:", "").strip()

    cart_item_id = "python-view-cart-test"

    add_response = requests.post(
        f"{BASE_URL}/addtocart",
        json={"id": cart_item_id, "cookie": auth_token, "prod_id": 1, "flag": True},
        timeout=10,
    )

    assert add_response.status_code == 200

    view_response = requests.post(
        f"{BASE_URL}/viewcart",
        json={"cookie": auth_token, "flag": True},
        timeout=10,
    )

    assert view_response.status_code == 200

    data = view_response.json()
    assert "Items" in data
    assert isinstance(data["Items"], list)
    assert any(item["id"] == cart_item_id for item in data["Items"])
