def test_delete_cart_item(api_client, auth_token):
    cart_item_id = "python-delete-cart-test"

    add_response = api_client.add_to_cart(
        auth_token,
        item_id=cart_item_id,
        product_id=1,
    )
    assert add_response.status_code == 200

    view_response = api_client.view_cart(auth_token)
    assert view_response.status_code == 200

    cart_data = view_response.json()
    matching_items = [
        item for item in cart_data["Items"] if item.get("id") == cart_item_id
    ]
    assert matching_items, "Test cart item was not found"

    actual_cart_id = matching_items[0]["id"]
    delete_response = api_client.delete_item(actual_cart_id)

    assert delete_response.status_code == 200
    assert delete_response.json() == "Item deleted."

    verify_response = api_client.view_cart(auth_token)
    assert verify_response.status_code == 200

    remaining_items = verify_response.json()["Items"]
    assert not any(item.get("id") == actual_cart_id for item in remaining_items)
