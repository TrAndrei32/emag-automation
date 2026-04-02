from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.product_page import ProductPage


def test_sort_by_price_descending(page):

    home = HomePage(page)
    home.search("iphone")

    search = SearchPage(page)
    assert search.results_are_visible()

    search.sort_by_price_descending()

    page.wait_for_load_state("networkidle")
    assert "pricedesc" in page.url.lower()

    assert search.results_are_visible()

    first_title = search.get_first_product_title()
    search.click_first_product()

    product = ProductPage(page)
    product.add_to_cart_button.wait_for(state="visible")
    assert product.is_add_to_cart_visible()

    print(f"\nProdus deschis: {product.get_title()}")
    print(f"Titlu din lista sortata: {first_title}")
