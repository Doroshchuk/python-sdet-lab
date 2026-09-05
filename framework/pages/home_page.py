from playwright.sync_api import Page

from framework.pages.base_page import BasePage
from framework.pages.components.product_listing import ProductListing
from framework.pages.login_page import LoginPage
from framework.pages.products_page import ProductsPage


class HomePage(BasePage):
    PATH = "/"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.signup_login_link = self.page.get_by_role("link", name="Signup / Login")
        self.products_link = self.page.get_by_role("link", name="Products")

        self.slider = self.page.locator("#slider")
        self.product_listing = ProductListing(self.page)

    def go_to_signup_login_page(self) -> LoginPage:
        self.signup_login_link.click()
        return LoginPage(self.page)

    def go_to_products_page(self) -> ProductsPage:
        self.products_link.click()
        return ProductsPage(self.page)
