import pytest
from playwright.sync_api import Playwright


@pytest.fixture(scope="session", autouse=True)
def configure_playwright(playwright: Playwright) -> None:
    playwright.selectors.set_test_id_attribute("data-qa")
