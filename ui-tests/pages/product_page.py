from playwright.sync_api import Page


class ProductPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart_link = 'a:has-text("Add to cart")'

    def add_to_cart(self):
        self.page.locator(self.add_to_cart_link).click()
