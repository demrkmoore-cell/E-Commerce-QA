from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_items = "#tbodyid tr"

    def navigate(self):
        self.page.goto("https://www.demoblaze.com/cart.html")

    def item_count(self):
        return self.page.locator(self.cart_items).count()
