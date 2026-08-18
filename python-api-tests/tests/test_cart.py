def test_add_product_to_cart(api_client, auth_token):
    response = api_client.add_to_cart(
        auth_token,
        item_id="python-test-cart-item",
        product_id=1,
    )

    assert response.status_code == 200
