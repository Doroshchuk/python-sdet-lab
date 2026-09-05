from playwright.sync_api import Page, expect

from framework.config.settings import BASE_URL
from framework.pages.home_page import HomePage
from framework.utils.common import build_url


def test_home_page_is_displayed(page: Page) -> None:
    home_page = HomePage(page)
    home_page.open()

    expect(home_page.page).to_have_url(build_url(BASE_URL, HomePage.PATH))
    expect(home_page.slider).to_be_visible()
