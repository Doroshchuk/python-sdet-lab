import re
from pathlib import Path

import allure
import pytest
from playwright.sync_api import Page, Playwright

from framework.pages.home_page import HomePage
from framework.pages.products_page import ProductsPage
from framework.pages.signup_and_login_page import SignupAndLoginPage


@pytest.fixture
def home_page(page: Page) -> HomePage:
    home_page = HomePage(page)
    home_page.open()
    return home_page


@pytest.fixture
def signup_login_page(page: Page) -> SignupAndLoginPage:
    signup_login_page = SignupAndLoginPage(page)
    signup_login_page.open()
    return signup_login_page


@pytest.fixture
def products_page(page: Page) -> ProductsPage:
    products_page = ProductsPage(page)
    products_page.open()
    return products_page


@pytest.fixture(scope="session", autouse=True)
def configure_playwright(playwright: Playwright) -> None:
    playwright.selectors.set_test_id_attribute("data-qa")


@pytest.fixture(autouse=True)
def block_ad_request(page: Page) -> None:
    """Block third-party ad requests that may cause flaky UI tests."""
    page.route("**/*doubleclick.net/**", lambda route: route.abort())


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call) -> None:
    outcome = yield
    report: pytest.TestReport = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)


# A regular expression to match the file names of the screenshots taken on test failures
SCREENSHOT_NAME_PATTERN = re.compile(r"^test-failed-\d+\.png$")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_teardown(item, nextitem):
    yield

    report: pytest.TestReport | None = getattr(item, "rep_call", None)

    if report is None or not report.failed:
        return

    artifacts_dir = item.funcargs.get("output_path")
    if not artifacts_dir:
        return

    artifacts_dir_path = Path(artifacts_dir)
    for file in artifacts_dir_path.iterdir():
        if file.is_file() and SCREENSHOT_NAME_PATTERN.match(file.name):
            allure.attach.file(
                str(file),
                name="Failure screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
