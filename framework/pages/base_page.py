from playwright.sync_api import Page

from framework.config.settings import BASE_URL
from framework.pages.components.header import Header
from framework.utils.common import build_url


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.header = Header(self.page)

    def open(self, path: str = "") -> None:
        self.page.goto(build_url(BASE_URL, path))
