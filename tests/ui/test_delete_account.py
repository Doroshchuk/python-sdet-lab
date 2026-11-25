from playwright.sync_api import expect

from framework.api.clients.user_client import UserApiClient
from framework.api.models.responses import BaseResponse
from framework.models.user_registration_data import UserRegistrationData
from framework.pages.home_page import HomePage


def test_delete_account_successfully(
    registered_user: UserRegistrationData,
    home_page: HomePage,
    user_api_client: UserApiClient,
) -> None:
    signup_login_page = home_page.header.go_to_signup_login_page()
    signup_login_page.login(registered_user.email, registered_user.password)

    expect(home_page.header.logged_in_as_link).to_have_text(
        f"Logged in as {registered_user.name}"
    )

    account_deleted_page = home_page.header.delete_account()
    expect(account_deleted_page.title).to_be_visible()
    account_deleted_page.continue_to_home_page()
    expect(home_page.header.signup_login_link).to_be_visible()

    get_response = user_api_client.get_account(registered_user.email)
    assert get_response.ok, get_response.text()
    get_result = BaseResponse.model_validate(get_response.json())
    assert get_result.response_code == 404, (
        f"Account shouldn`t longer exist {get_result.text()}"
    )
