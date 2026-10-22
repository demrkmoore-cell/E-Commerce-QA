from playwright.sync_api import Page


class ProductPage:
    def __init__(self, page: Page):
        self.page = page
        self.product_title = "#tbodyid h2"
        self.product_price = "#tbodyid h3"
        self.product_description = "#more-information"
        self.add_to_cart_link = 'a:has-text("Add to cart")'

    def add_to_cart(self):
        self.page.locator(self.add_to_cart_link).click()

    def get_title(self):
        return self.page.locator(self.product_title).inner_text()

    def get_price(self):
        return self.page.locator(self.product_price).inner_text()

    def get_description(self):
        return self.page.locator(self.product_description).inner_text()
