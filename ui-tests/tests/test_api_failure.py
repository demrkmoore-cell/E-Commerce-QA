from playwright.sync_api import expect


def test_product_api_failure_does_not_display_products(page):
    page.route(
        "https://api.demoblaze.com/entries",
        lambda route: route.fulfill(
            status=500,
            body="Internal Server Error",
        ),
    )

    with page.expect_response(
        lambda response: (
            response.url.endswith("/entries")
            and response.status == 500
        )
    ) as response_info:
        page.goto(
            "https://www.demoblaze.com/",
            wait_until="networkidle",
        )

    assert response_info.value.status == 500
    expect(page.locator(".card")).to_have_count(0)
