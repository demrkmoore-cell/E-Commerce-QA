def test_add_to_cart_null_request_id_exposes_server_error(api_client, auth_token):
    response = api_client.post(
        "/addtocart",
        json={
            "id": None,
            "cookie": auth_token,
            "prod_id": 1,
            "flag": True,
        },
    )

    # Regression documentation for Jira EQAP-10:
    # invalid client input currently produces a server-side 500 response.
    assert response.status_code == 500
