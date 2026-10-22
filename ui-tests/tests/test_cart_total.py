from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


def test_cart_total_matches_selected_product_price(page):
    home_page = HomePage(page)
    product_page = ProductPage(page)
    cart_page = CartPage(page)

    home_page.navigate()
    home_page.select_first_product()

    page.locator(product_page.product_title).wait_for(state="visible")
    selected_price = product_page.get_price().replace("$", "").split("*")[0].strip()

    page.on("dialog", lambda dialog: dialog.accept())
    # Wait for the add-to-cart API request to complete before opening the cart.
    # This prevents a CI timing race where cart.html loads before the item is persisted.
    with page.expect_response(
        lambda response: "/addtocart" in response.url
        and response.request.method == "POST"
        and response.status == 200
    ):
        product_page.add_to_cart()

    cart_page.navigate()

    page.locator(cart_page.cart_items).first.wait_for(state="visible")
    page.locator("#totalp").wait_for(state="visible")

    cart_item_price = cart_page.get_first_item_price().replace("$", "").strip()
    cart_total = cart_page.get_total().replace("$", "").strip()

    assert cart_item_price == selected_price
    assert cart_total == selected_price
