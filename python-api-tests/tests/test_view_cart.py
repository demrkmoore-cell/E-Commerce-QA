def test_view_cart_contains_product(api_client, auth_token):
    cart_item_id = "python-view-cart-test"

    add_response = api_client.add_to_cart(
        auth_token,
        item_id=cart_item_id,
        product_id=1,
    )
    assert add_response.status_code == 200

    view_response = api_client.view_cart(auth_token)
    assert view_response.status_code == 200

    data = view_response.json()
    assert "Items" in data
    assert isinstance(data["Items"], list)
    assert any(item.get("id") == cart_item_id for item in data["Items"])
