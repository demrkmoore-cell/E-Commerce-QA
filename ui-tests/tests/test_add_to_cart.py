from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


def test_add_product_to_cart(page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.select_first_product()

    product_page = ProductPage(page)
    product_page.add_to_cart()

    cart_page = CartPage(page)
    cart_page.navigate()
    page.locator("#tbodyid tr").first.wait_for(state="visible")

    assert cart_page.item_count() > 0
