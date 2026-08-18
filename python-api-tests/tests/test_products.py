import requests


BASE_URL = "https://api.demoblaze.com"


def test_get_products():
    response = requests.get(
        f"{BASE_URL}/entries",
        timeout=10,
    )

    assert response.status_code == 200

    data = response.json()

    assert "Items" in data
    assert isinstance(data["Items"], list)
    assert data["Items"], "Products list should not be empty"

    for product in data["Items"]:
        assert "id" in product
        assert "title" in product
        assert "price" in product
        assert "cat" in product
