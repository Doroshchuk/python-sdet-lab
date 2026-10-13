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
def signup_login_page(page: Page) -> SignupAndLoginPage:
    signup_login_page = SignupAndLoginPage(page)
    signup_login_page.open()
    return signup_login_page


@pytest.fixture
def products_page(page: Page) -> ProductsPage:
    products_page = ProductsPage(page)
    products_page.open()
    return products_page
