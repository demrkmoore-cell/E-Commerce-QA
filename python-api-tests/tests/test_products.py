def test_get_products(api_client):
    response = api_client.get("/entries")

    assert response.status_code == 200
    data = response.json()

    assert "Items" in data
    assert isinstance(data["Items"], list)
    assert data["Items"], "Products list should not be empty"

    for product in data["Items"]:
        assert product.get("id") is not None
        assert product.get("title")
        assert isinstance(product.get("price"), (int, float))
        assert product.get("cat")
