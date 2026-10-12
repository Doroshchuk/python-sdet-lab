from playwright.sync_api import Page

from framework.pages.base_page import BasePage
from framework.pages.signup_page import SignupPage


class SignupAndLoginPage(BasePage):
    PATH = "/login"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        # Login
        self.login_form_title = self.page.get_by_role(
            "heading", name="Login to your account"
        )
        self.login_email_input = self.page.get_by_test_id("login-email")
        self.login_password_input = self.page.get_by_test_id("login-password")
        self.login_button = self.page.get_by_role("button", name="Login")
        self.login_error = self.page.get_by_text(
            "Your email or password is incorrect!", exact=True
        )

        # Signup
        self.signup_form_title = self.page.get_by_role(
            "heading", name="New User Signup!"
        )
        self.signup_name_input = self.page.get_by_test_id("signup-name")
        self.signup_email_input = self.page.get_by_test_id("signup-email")
        self.signup_button = self.page.get_by_role("button", name="Signup")

    def open(self) -> None:
        super().open(self.PATH)

    def login(self, email: str, password: str) -> None:
        self.login_email_input.fill(email)
        self.login_password_input.fill(password)
        self.login_button.click()

    def signup(self, name: str, email: str) -> SignupPage:
        self.signup_name_input.fill(name)
        self.signup_email_input.fill(email)
        self.signup_button.click()
        return SignupPage(self.page)
