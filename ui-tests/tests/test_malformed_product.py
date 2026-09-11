def test_malformed_product_id_does_not_display_product(page):
    page.goto("https://www.demoblaze.com/prod.html?idp_=abc")

    product_title = page.locator("#tbodyid h2")

    assert product_title.count() == 0
