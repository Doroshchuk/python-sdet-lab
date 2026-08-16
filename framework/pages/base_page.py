from playwright.sync_api import Page

from framework.config.settings import BASE_URL
from python.basics.functions import functions


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def open(self, path: str = "") -> None:
        self.page.goto(functions.build_url(BASE_URL, path))
