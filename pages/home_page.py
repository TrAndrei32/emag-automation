from playwright.sync_api import Page


class HomePage:

    def __init__(self, page: Page):
        self.page = page

        self.search_input = page.locator("input#searchboxTrigger")
        self.search_button = page.locator("button.searchbox-submit-button")

    def search(self, keyword: str):
        self.search_input.fill(keyword)
        self.search_button.click()

    def get_title(self):
        return self.page.title()
