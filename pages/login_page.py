from playwright.sync_api import Page
from utils.config import BASE_URL


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

        self.account_button = page.locator("a[aria-label='Contul meu']")
        self.email_input = page.locator("#user_login_email")

    def navigate(self):
        self.page.goto(BASE_URL)
        self.account_button.click()

    def enter_email(self, email: str):
        self.email_input.fill(email)

    def is_email_input_visible(self):
        self.email_input.wait_for(state="visible")
        return self.email_input.is_visible()
