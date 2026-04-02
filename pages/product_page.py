from playwright.sync_api import Page


class ProductPage:

    def __init__(self, page: Page):
        self.page = page

        self.add_to_cart_button = page.locator(
            "[data-test='main-add-to-cart-button']")
        self.product_title = page.locator("h1").first

    def add_to_cart(self):
        self.add_to_cart_button.click()

    def get_title(self):
        return self.product_title.inner_text()

    def is_add_to_cart_visible(self):
        self.add_to_cart_button.wait_for(state="visible")
        return self.add_to_cart_button.is_visible()
