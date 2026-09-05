import pytest
from playwright.sync_api import Page

from framework.pages.home_page import HomePage


@pytest.fixture
def home_page(page: Page) -> HomePage:
    home_page = HomePage(page)
    home_page.open()
    return home_page
