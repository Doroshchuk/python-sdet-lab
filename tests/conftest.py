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
            response = api_request_context.delete(
                url="/api/deleteAccount", form={"email": email, "password": password}
            )
            assert response.json()["responseCode"] == 200

        request.addfinalizer(cleanup)

    return register
