from collections.abc import Callable

import pytest
from playwright.sync_api import expect

from framework.models.user_registration_data import UserRegistrationData
from framework.pages.home_page import HomePage
from framework.pages.signup_and_login_page import SignupAndLoginPage


# Test Case 1
@pytest.mark.smoke
def test_register_successfully(
    home_page: HomePage,
    signup_login_page: SignupAndLoginPage,
    user_registration_data: UserRegistrationData,
    register_user_cleanup: Callable[[str, str], None],
) -> None:
    register_user_cleanup(user_registration_data.email, user_registration_data.password)
    signup_page = signup_login_page.signup(
        name=user_registration_data.name, email=user_registration_data.email
    )

    expect(signup_page.account_info_title).to_be_visible()

    account_created_page = signup_page.create_account(user_registration_data)

    expect(account_created_page.title).to_be_visible()

    account_created_page.proceed()

    expect(home_page.header.logged_in_as_link).to_be_visible()
    expect(home_page.header.logged_in_as_link).to_have_text(
        f"Logged in as {user_registration_data.name}"
    )
