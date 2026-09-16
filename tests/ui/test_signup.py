from playwright.sync_api import expect

from framework.factories.user_registration_data_factory import (
    UserRegistrationDataFactory,
)
from framework.pages.home_page import HomePage


# Test Case 1
def test_register_successfully(home_page: HomePage) -> None:
    signup_login_page = home_page.go_to_signup_login_page()

    expect(signup_login_page.signup_form_title).to_be_visible()

    user_registration_data = UserRegistrationDataFactory.create()
    signup_page = signup_login_page.signup(
        name=user_registration_data.name, email=user_registration_data.email
    )

    expect(signup_page.account_info_title).to_be_visible()

    account_created_page = signup_page.create_account(user_registration_data)

    expect(account_created_page.title).to_be_visible()

    account_created_page.proceed()

    expect(home_page.logged_in_as_link).to_be_visible()
    expect(home_page.logged_in_as_link).to_have_text(
        f"Logged in as {user_registration_data.name}"
    )

    account_deleted_page = home_page.delete_account()

    expect(account_deleted_page.title).to_be_visible()

    account_deleted_page.continue_to_home_page()
