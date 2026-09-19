from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


def test_add_product_to_cart(page):
    home_page = HomePage(page)
    product_page = ProductPage(page)
    cart_page = CartPage(page)

    home_page.navigate()
    home_page.select_first_product()

    page.locator(product_page.product_title).wait_for(state="visible")
    selected_product = product_page.get_title()

    page.on("dialog", lambda dialog: dialog.accept())
    product_page.add_to_cart()
    cart_page.navigate()

    page.locator(cart_page.cart_items).first.wait_for(state="visible")

    assert cart_page.item_count() > 0
    assert selected_product in page.locator(cart_page.cart_items).first.inner_text()
