from playwright.sync_api import expect


def test_invalid_product_id_does_not_render_product_details(page):
    with page.expect_response(
        lambda response: response.url.endswith("/view")
        and response.request.method == "POST"
    ):
        page.goto(
            "https://www.demoblaze.com/prod.html?idp_=999999",
            wait_until="domcontentloaded",
        )

    product_title = page.locator("#tbodyid h2")
    product_price = page.locator("#tbodyid h3")
    add_to_cart = page.get_by_role("link", name="Add to cart")

    # Invalid product data must not be rendered as if it were valid.
    expect(product_title).to_have_count(0, timeout=10000)
    expect(product_price).to_have_count(0, timeout=10000)
    expect(add_to_cart).to_have_count(0, timeout=10000)
