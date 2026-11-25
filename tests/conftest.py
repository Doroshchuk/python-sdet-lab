import pytest
from playwright.sync_api import APIRequestContext, Playwright

from framework.api.clients.user_client import UserApiClient
from framework.api.models.responses import BaseResponse
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
            get_response = user_api_client.get_account(email)
            assert get_response.ok, get_response.text()
            get_result = BaseResponse.model_validate(get_response.json())
            if get_result.response_code == 404:
                return

            assert get_result.response_code == 200, (
                f"Unexpected response during account lookup: {get_response.text()}"
            )
            delete_response = user_api_client.delete_account(email, password)
            assert delete_response.ok, delete_response.text()
            delete_result = BaseResponse.model_validate(delete_response.json())
            assert delete_result.response_code == 200, (
                f"Account cleanup failed for {email}: {delete_response.text()}"
            )

        request.addfinalizer(cleanup)

    return register
