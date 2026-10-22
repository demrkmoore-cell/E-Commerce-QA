from pages.home_page import HomePage


def test_select_product(page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.select_first_product()

    page.locator(".name").wait_for(state="visible")
    assert page.locator(".name").is_visible()
    assert page.locator(".price-container").is_visible()
