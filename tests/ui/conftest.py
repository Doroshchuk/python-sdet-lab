import pytest
from playwright.sync_api import Page

from framework.pages.home_page import HomePage
from framework.pages.products_page import ProductsPage
from framework.pages.signup_and_login_page import SignupAndLoginPage


@pytest.fixture
def home_page(page: Page) -> HomePage:
    home_page = HomePage(page)
    home_page.open()
    return home_page


@pytest.fixture
def signup_login_page(home_page: HomePage) -> SignupAndLoginPage:
    return home_page.header.go_to_signup_login_page()


@pytest.fixture
def products_page(home_page: HomePage) -> ProductsPage:
    return home_page.header.go_to_products_page()
