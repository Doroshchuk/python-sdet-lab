from playwright.sync_api import Page

from framework.pages.base_page import BasePage


class ProductsPage(BasePage):
    PATH = "/products"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.all_products_title = self.page.get_by_role("heading", name="All Products")
        self.search_input = self.page.get_by_role("textbox", name="search")
        self.search_button = self.page.locator("#submit_search")
        self.product_cards = self.page.locator(".single-products")
        self.searched_products_title = self.page.get_by_role(
            "heading", name="Searched Products"
        )

    def search_product(self, search_term: str) -> None:
        self.search_input.fill(search_term)
        self.search_button.click()

    def product_titles(self) -> list[str]:
        return self.product_cards.locator(".overlay-content  p").all_text_contents()
