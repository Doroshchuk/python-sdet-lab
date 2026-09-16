from __future__ import annotations

from typing import TYPE_CHECKING

from playwright.sync_api import Page

if TYPE_CHECKING:
    from framework.pages.account_deleted_page import AccountDeletedPage
    from framework.pages.products_page import ProductsPage
    from framework.pages.signup_login_page import SignupAndLoginPage


class Header:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.signup_login_link = self.page.get_by_role("link", name="Signup / Login")
        self.products_link = self.page.get_by_role("link", name="Products")
        self.logged_in_as_link = self.page.locator("#header a").filter(
            has_text="Logged in as"
        )
        self.delete_account_link = self.page.get_by_role("link", name="Delete Account")

    def go_to_signup_login_page(self) -> SignupAndLoginPage:
        from framework.pages.signup_login_page import SignupAndLoginPage

        self.signup_login_link.click()
        return SignupAndLoginPage(self.page)

    def go_to_products_page(self) -> ProductsPage:
        from framework.pages.products_page import ProductsPage

        self.products_link.click()
        return ProductsPage(self.page)

    def delete_account(self) -> AccountDeletedPage:
        from framework.pages.account_deleted_page import AccountDeletedPage

        self.delete_account_link.click()
        return AccountDeletedPage(self.page)
