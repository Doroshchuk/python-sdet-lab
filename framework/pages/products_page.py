from playwright.sync_api import Page

from framework.pages.base_page import BasePage
from framework.pages.components.product_card import ProductCard


class ProductsPage(BasePage):
    PATH = "/products"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.all_products_title = self.page.get_by_role("heading", name="All Products")
        self.search_input = self.page.get_by_role("textbox", name="search")
        self.search_button = self.page.locator("#submit_search")
        self.product_cards = self.page.locator(".product-image-wrapper")
        self.searched_products_title = self.page.get_by_role(
            "heading", name="Searched Products"
        )

    def product_at(self, index: int) -> ProductCard:
        return ProductCard(self.page, self.product_cards.nth(index))

    def product_card(self, product_title: str) -> ProductCard:
        title = self.page.locator(".productinfo").get_by_text(product_title, exact=True)
        card = self.product_cards.filter(has=title)
        return ProductCard(self.page, card)

    def search_product(self, search_term: str) -> None:
        self.search_input.fill(search_term)
        self.search_button.click()

    def product_titles(self) -> list[str]:
        return self.product_cards.locator(".productinfo p").all_text_contents()
