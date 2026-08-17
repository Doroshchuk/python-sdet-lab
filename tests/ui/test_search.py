from playwright.sync_api import Page, expect

from framework.config.settings import BASE_URL
from framework.pages.home_page import HomePage
from framework.pages.products_page import ProductsPage
from framework.utils.common import build_url


def test_search_products(page: Page) -> None:
    home_page = HomePage(page)
    home_page.open()
    products_page = home_page.go_to_products_page()

    expect(products_page.page).to_have_url(build_url(BASE_URL, ProductsPage.PATH))
    expect(products_page.all_products_title).to_be_visible()

    search_term = "dress"
    products_page.search_product(search_term)
    expect(products_page.searched_products_title).to_be_visible()
    expect(products_page.product_cards).not_to_have_count(0)
    expect(products_page.product_cards.first).to_be_visible()

    # TODO: Validate search result relevance once the expected search behavior is defined.
    # Searching for "dress" currently returns products whose titles do not contain
    # "dress" (e.g. "Sleeveless Unicorn Patch Gown - Pink"), so title matching
    # cannot reliably determine whether all returned products are relevant.

    # product_titles = products_page.product_titles()
    # assert product_titles, "No products found"
    # assert all(search_term.lower() in title.lower() for title in product_titles), (
    #     f"Some products don`t match '{search_term}': {product_titles}"
    # )
