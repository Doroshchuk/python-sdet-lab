import pytest
from playwright.sync_api import APIRequestContext, Playwright

from framework.api.clients.user_client import UserApiClient
from framework.api.models.responses import BaseResponse, UserAccountResponse
from framework.config.settings import BASE_URL


@pytest.fixture
def api_request_context(playwright: Playwright) -> APIRequestContext:
    context = playwright.request.new_context(base_url=BASE_URL)
    yield context
    context.dispose()


@pytest.fixture
def user_api_client(api_request_context: APIRequestContext) -> UserApiClient:
    return UserApiClient(api_request_context)


@pytest.fixture
def register_user_cleanup(
    request: pytest.FixtureRequest, user_api_client: UserApiClient
):
    def register(email: str, password: str):
        def cleanup():
            account_response = user_api_client.get_account(email)
            assert account_response.ok
            account_response_data = BaseResponse.model_validate(account_response.json())
            if account_response_data.response_code == 404:
                return

            assert account_response_data.response_code == 200, (
                f"Unexpected response during account lookup: "
                f"{account_response.text()}"
            )
            delete_response = user_api_client.delete_account(email, password)
            assert delete_response.ok
            delete_response_data = BaseResponse.model_validate(delete_response.json())
            assert delete_response_data.response_code == 200, (
                f"Account cleanup failed for {email}: "
                f"{delete_response.text()}"
            )

        request.addfinalizer(cleanup)

    return register
