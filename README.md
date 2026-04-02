# eMAG Automation Testing Project

UI test automation project built with **Python + Playwright + pytest** on the live website [eMAG.ro](https://www.emag.ro).

## Tech Stack

- Python 3.14
- Playwright (browser automation)
- pytest (test runner)
- pytest-html (HTML reports)
- Page Object Model (POM)

## Project Structure
```
emag-automation/
├── pages/
│   ├── home_page.py          # Homepage - search functionality
│   ├── search_page.py        # Search results - sorting & filters
│   ├── product_page.py       # Product page - add to cart button
│   └── login_page.py         # Authentication page
├── tests/
│   ├── 01_test_login.py      # Login flow test
│   ├── 02_test_navigation.py # Category navigation test
│   ├── 03_test_search.py     # Search functionality tests
│   └── 04_test_filters.py    # Sorting and filter test
├── utils/
│   └── config.py             # Global configuration
├── reports/                  # Auto-generated HTML reports
├── conftest.py               # Browser setup
└── pytest.ini                # pytest configuration
```

## Test Scenarios

| Test | Description | Status |
|------|-------------|--------|
| test_login_page_flow | Navigate to login, enter email | ✅ |
| test_navigate_to_playstation_category | Navigate to Sony PlayStation category page | ✅ |
| test_search_returns_results | Search for a product and verify results are displayed | ✅ |
| test_add_first_product_to_cart | Search, open first product, verify add to cart button | ✅ |
| test_sort_by_price_descending | Sort search results by descending price | ✅ |

## Getting Started

### Install dependencies
```bash
pip install playwright pytest pytest-html pytest-metadata
playwright install
```

### Run tests
```bash
# Run all tests
pytest -v

# Run a single file
pytest tests/03_test_search.py -v

# Run with printed output
pytest -v -s
```

### HTML Report

After running tests, open `reports/report.html` in your browser.

## Key Concepts Demonstrated

- **Page Object Model (POM)** — locators and actions separated from test logic
- **Fixtures** — automatic browser setup via `conftest.py`
- **Explicit Waits** — handling dynamic elements with `wait_for(state="visible")`
- **Stable Selectors** — using CSS selectors and `data-test` attributes
- **Centralized Config** — base URL, timeout and headless mode in one place
- **Real Website Testing** — automation on a live e-commerce platform