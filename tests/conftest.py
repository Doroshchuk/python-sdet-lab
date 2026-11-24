import pytest
from playwright.sync_api import APIRequestContext, Playwright

from framework.config.settings import BASE_URL


@pytest.fixture
def api_request_context(playwright: Playwright) -> APIRequestContext:
    context = playwright.request.new_context(base_url=BASE_URL)
    yield context
    context.dispose()


@pytest.fixture
def register_user_cleanup(
    request: pytest.FixtureRequest, api_request_context: APIRequestContext
):
    def register(email: str, password: str):
        def cleanup():
            account_response = api_request_context.get(
                url="/api/getUserDetailByEmail",
                params={"email": email}
            )
            assert account_response.ok
            account_response_code = account_response.json()["responseCode"]
            if account_response_code == 404:
                return

            assert account_response_code == 200, (
                f"Unexpected response during account lookup: "
                f"{account_response.text()}"
            )
            delete_response = api_request_context.delete(
                url="/api/deleteAccount", form={"email": email, "password": password}
            )
            assert delete_response.ok
            assert delete_response.json()["responseCode"] == 200, (
                f"Account cleanup failed for {email}: "
                f"{delete_response.text()}"
            )

        request.addfinalizer(cleanup)

    return register
