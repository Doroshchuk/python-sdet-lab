import pytest
from playwright.sync_api import Page, Playwright


@pytest.fixture(scope="session", autouse=True)
def configure_playwright(playwright: Playwright) -> None:
    playwright.selectors.set_test_id_attribute("data-qa")


@pytest.fixture(autouse=True)
def block_ad_request(page: Page) -> None:
    """Block third-party ad requests that may cause flaky UI tests."""
    page.route("**/*doubleclick.net/**", lambda route: route.abort())
