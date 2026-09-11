def test_invalid_product_id_does_not_display_product(page):
    page.goto("https://www.demoblaze.com/prod.html?idp_=999999")

    product_title = page.locator("#tbodyid h2")

    assert product_title.count() == 0
