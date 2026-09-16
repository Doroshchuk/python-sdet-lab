from playwright.sync_api import Page

from framework.pages.base_page import BasePage


class AccountCreatedPage(BasePage):
    PATH = "/account_created"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.title = self.page.get_by_role("heading", name="Account Created!")
        self.continue_button = self.page.get_by_test_id("continue-button")

    def proceed(self) -> None:
        self.continue_button.click()
