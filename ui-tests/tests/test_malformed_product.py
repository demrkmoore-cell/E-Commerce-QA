def test_malformed_product_id_does_not_display_product(page):
    page.goto("https://www.demoblaze.com/prod.html?idp_=abc", wait_until="domcontentloaded")

    page.locator("#tbodyid").wait_for(state="visible")
    product_title = page.locator("#tbodyid h2")

    assert product_title.count() == 0
