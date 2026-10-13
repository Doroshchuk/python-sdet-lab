from playwright.sync_api import expect

from framework.pages.products_page import ProductsPage


# Test Case 9
def test_search_products(products_page: ProductsPage) -> None:
    search_term = "dress"
    products_page.search_product(search_term)
    expect(products_page.product_listing.title).to_be_visible()
    expect(products_page.product_listing.title).to_have_text("Searched Products")
    expect(products_page.product_listing.product_cards).not_to_have_count(0)
    for product_card in products_page.product_listing.product_cards.all():
        expect(product_card).to_be_visible()

    # TODO: Validate search result relevance once the expected search behavior is defined.
    # Searching for "dress" currently returns products whose titles do not contain
    # "dress" (e.g. "Sleeveless Unicorn Patch Gown - Pink"), so title matching
    # cannot reliably determine whether all returned products are relevant.

    # product_titles = products_page.product_listing.product_titles()
    # assert product_titles, "No products found"
    # assert all(search_term.lower() in title.lower() for title in product_titles), (
    #     f"Some products don`t match '{search_term}': {product_titles}"
    # )
