from playwright.sync_api import Page


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://www.demoblaze.com/"
        self.product_cards = ".card"

    def navigate(self):
        self.page.goto(self.url)
        self.page.locator(self.product_cards).first.wait_for(state="visible")

    def product_count(self):
        return self.page.locator(self.product_cards).count()

    def select_first_product(self):
        self.page.locator(".card-title").first.click()
