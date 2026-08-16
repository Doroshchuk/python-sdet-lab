from playwright.sync_api import Page

from framework.pages.base_page import BasePage


class LoginPage(BasePage):
    PATH = "/login"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.login_form_title = self.page.get_by_role(
            "heading", name="Login to your account"
        )
        self.email_input = self.page.get_by_test_id("login-email")
        self.password_input = self.page.get_by_test_id("login-password")
        self.login_button = self.page.get_by_role("button", name="Login")
        self.login_error = self.page.get_by_text("Your email or password is incorrect!")

    def open(self) -> None:
        super().open(self.PATH)

    def login(self, email: str, password: str) -> None:
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()
