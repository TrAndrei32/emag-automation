from playwright.sync_api import Page


class SearchPage:

    def __init__(self, page: Page):
        self.page = page

        self.product_cards = page.locator(".card-item")
        self.product_titles = page.locator(".card-v2-title")
        self.sort_button = page.locator("button.sort-control-btn")
        self.sort_price_desc = page.locator(
            "a[data-sort-id='price'][data-sort-dir='desc']")

    def get_results_count(self):
        return self.product_cards.count()

    def get_first_product_title(self):
        return self.product_titles.first.inner_text()

    def results_are_visible(self):
        return self.product_cards.count() > 0

    def click_first_product(self):
        self.product_titles.first.click()

    def sort_by_price_descending(self):
        self.sort_button.first.click()
        self.sort_price_desc.wait_for(state="visible")
        self.sort_price_desc.click()
