import pytest
from playwright.sync_api import sync_playwright
from utils.config import BASE_URL, DEFAULT_TIMEOUT, HEADLESS, SLOW_MO


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS, slow_mo=SLOW_MO)
        context = browser.new_context()
        page = context.new_page()
        page.set_default_timeout(DEFAULT_TIMEOUT)
        page.goto(BASE_URL)
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
