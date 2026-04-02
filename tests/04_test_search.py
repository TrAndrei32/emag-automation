from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.product_page import ProductPage


def test_search_returns_results(page):
    home = HomePage(page)
    home.search("iphone")

    search = SearchPage(page)

    assert "iphone" in page.url.lower()
    assert search.results_are_visible()
    assert search.get_results_count() > 0

    print(f"\nPrimul produs: {search.get_first_product_title()}")
    print(f"Total produse vizibile: {search.get_results_count()}")


def test_add_first_product_to_cart(page):

    home = HomePage(page)
    home.search("iphone")

    search = SearchPage(page)
    first_product_title = search.get_first_product_title()
    search.click_first_product()

    product = ProductPage(page)
    assert product.is_add_to_cart_visible()

    print(f"\nProdus deschis: {product.get_title()}")
    print(f"Titlu din search: {first_product_title}")
