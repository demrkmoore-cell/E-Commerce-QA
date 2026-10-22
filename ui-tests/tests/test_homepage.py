from pages.home_page import HomePage


def test_homepage_displays_products(page):
    home_page = HomePage(page)
    home_page.navigate()

    assert page.title() == "STORE"
    assert home_page.product_count() > 0
