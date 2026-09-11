def test_product_api_failure_does_not_display_products(page):
    page.route(
        "https://api.demoblaze.com/entries",
        lambda route: route.fulfill(
            status=500,
            body="Internal Server Error"
        )
    )

    page.goto("https://www.demoblaze.com/")
    page.wait_for_timeout(1000)

    assert page.locator(".card").count() == 0
