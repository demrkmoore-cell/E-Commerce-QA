from pages.home_page import HomePage
from pages.product_page import ProductPage


def test_product_details_are_displayed(page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.select_first_product()

    product_page = ProductPage(page)

    assert product_page.get_title() != ""
    assert product_page.get_price() != ""
    assert product_page.get_description() != ""
