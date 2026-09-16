from playwright.sync_api import Page

from framework.pages.base_page import BasePage


class AccountDeletedPage(BasePage):
    PATH = "/delete_account"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.title = self.page.get_by_role("heading", name="Account Deleted!")
        self.continue_button = self.page.get_by_test_id("continue-button")

    def continue_to_home_page(self) -> None:
        self.continue_button.click()
