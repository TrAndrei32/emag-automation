# from playwright.sync_api import Page
from pages.search_page import SearchPage


def test_navigate_to_playstation_category(page):

    page.goto(
        "https://www.emag.ro/console-hardware/brand/sony/c?ref=hp_menu_quick-nav_463_1&type=link")

    page.wait_for_load_state("networkidle")
    assert "console-hardware" in page.url.lower()

    title = page.locator("h1").first.inner_text()
    assert "Sony" in title or "Console" in title

    search = SearchPage(page)
    assert search.results_are_visible()

    print(f"\nPagina: {title}")
    print(f"URL: {page.url}")
    print(f"Produse gasite: {search.get_results_count()}")
