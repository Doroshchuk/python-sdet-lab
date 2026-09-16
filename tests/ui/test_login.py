from playwright.sync_api import expect

from framework.pages.home_page import HomePage
from framework.utils.common import (
    generate_random_email,
    generate_random_string,
)


# Test Case 3
def test_login_with_invalid_credentials(home_page: HomePage) -> None:
    login_page = home_page.header.go_to_signup_login_page()

    expect(login_page.login_form_title).to_be_visible()
    login_page.login(generate_random_email(), generate_random_string())
    expect(login_page.login_error).to_be_visible()
