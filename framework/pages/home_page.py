from playwright.sync_api import Page

from framework.pages.base_page import BasePage
from framework.pages.components.product_listing import ProductListing


class HomePage(BasePage):
    PATH = "/"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.slider = self.page.locator("#slider")
        self.product_listing = ProductListing(self.page)
