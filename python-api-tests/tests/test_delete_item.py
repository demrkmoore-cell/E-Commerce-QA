import os
import requests

BASE_URL = "https://api.demoblaze.com"


def test_delete_cart_item():
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

    cart_item_id = "python-delete-cart-test"

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

    cart_data = view_response.json()
    matching_items = [item for item in cart_data["Items"] if item["id"] == cart_item_id]
    assert matching_items, "Test cart item was not found"

    actual_cart_id = matching_items[0]["id"]

    delete_response = requests.post(
        f"{BASE_URL}/deleteitem",
        json={"id": actual_cart_id},
        timeout=10,
    )

    assert delete_response.status_code == 200
    assert delete_response.json() == "Item deleted."

    verify_response = requests.post(
        f"{BASE_URL}/viewcart",
        json={"cookie": auth_token, "flag": True},
        timeout=10,
    )

    assert verify_response.status_code == 200

    remaining_items = verify_response.json()["Items"]
    assert not any(item["id"] == actual_cart_id for item in remaining_items)
