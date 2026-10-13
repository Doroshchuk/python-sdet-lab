from playwright.sync_api import Page

from framework.config.settings import BASE_URL
from framework.pages.base_page import BasePage
from framework.pages.components.product_listing import ProductListing
from framework.utils.common import build_url


class ProductsPage(BasePage):
    PATH = "/products"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.search_input = self.page.get_by_role("textbox", name="search")
        self.search_button = self.page.locator("#submit_search")
        self.product_listing = ProductListing(self.page)

    def open(self) -> None:
        self.page.goto(build_url(BASE_URL, ProductsPage.PATH))

    def search_product(self, search_term: str) -> None:
        self.search_input.fill(search_term)
        self.search_button.click()
