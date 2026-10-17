def test_invalid_product_id_returns_not_found_from_api(page):
    with page.expect_response(
        lambda response: response.url.endswith("/view")
        and response.request.method == "POST"
    ) as response_info:
        page.goto(
            "https://www.demoblaze.com/prod.html?idp_=999999",
            wait_until="domcontentloaded",
        )

    response = response_info.value

    assert response.status == 200
    assert response.json() == {"errorMessage": "Not found."}
