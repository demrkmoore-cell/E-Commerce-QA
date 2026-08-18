import os

import requests


BASE_URL = os.getenv("DEMOBLAZE_BASE_URL", "https://api.demoblaze.com")


class DemoblazeAPIClient:
    """Small reusable client for the Demoblaze REST API."""

    def __init__(self, base_url: str = BASE_URL):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

    def post(self, endpoint: str, **kwargs) -> requests.Response:
        kwargs.setdefault("timeout", 10)
        return self.session.post(f"{self.base_url}{endpoint}", **kwargs)

    def get(self, endpoint: str, **kwargs) -> requests.Response:
        kwargs.setdefault("timeout", 10)
        return self.session.get(f"{self.base_url}{endpoint}", **kwargs)

    def login(self, username: str, password: str) -> requests.Response:
        return self.post(
            "/login",
            json={"username": username, "password": password},
        )

    def add_to_cart(self, auth_token: str, item_id: str, product_id: int) -> requests.Response:
        return self.post(
            "/addtocart",
            json={
                "id": item_id,
                "cookie": auth_token,
                "prod_id": product_id,
                "flag": True,
            },
        )

    def view_cart(self, auth_token: str) -> requests.Response:
        return self.post(
            "/viewcart",
            json={"cookie": auth_token, "flag": True},
        )

    def delete_item(self, item_id: str) -> requests.Response:
        return self.post("/deleteitem", json={"id": item_id})


def credentials() -> tuple[str, str]:
    username = os.getenv("DEMOBLAZE_USERNAME")
    password = os.getenv("DEMOBLAZE_PASSWORD")

    if not username:
        raise AssertionError("DEMOBLAZE_USERNAME is not set")
    if not password:
        raise AssertionError("DEMOBLAZE_PASSWORD is not set")

    return username, password


def extract_auth_token(response: requests.Response) -> str:
    data = response.json()
    if not isinstance(data, str) or not data.startswith("Auth_token:"):
        raise AssertionError(f"Unexpected login response: {data!r}")

    token = data.replace("Auth_token:", "", 1).strip()
    if not token:
        raise AssertionError("Authentication token is empty")

    return token
