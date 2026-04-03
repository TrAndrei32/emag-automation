import pytest
from playwright.sync_api import sync_playwright
from utils.config import BASE_URL, DEFAULT_TIMEOUT, HEADLESS, SLOW_MO


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS, slow_mo=SLOW_MO)
        context = browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                                      viewport={"width": 1920, "height": 1080}
                                      )
        page = context.new_page()
        page.set_default_timeout(DEFAULT_TIMEOUT)
        page.goto(BASE_URL)

        try:
            cookie_button = page.locator("#onetrust-accept-btn-handler")
            cookie_button.wait_for(state="visible", timeout=5000)
            cookie_button.click()
        except:
            pass

        yield page
        context.close()
        browser.close()


def pytest_configure(config):
    config._metadata = {
        "Proiect": "eMAG Automation",
        "Autor": "Andrei",
        "Framework": "Playwright + pytest",
        "Site testat": "www.emag.ro"
    }
