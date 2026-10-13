from playwright.sync_api import expect

from framework.config.settings import BASE_URL
from framework.pages.home_page import HomePage
from framework.pages.products_page import ProductsPage
from framework.pages.signup_and_login_page import SignupAndLoginPage
from framework.utils.common import build_url


def test_home_page_is_displayed(home_page: HomePage) -> None:
    expect(home_page.page).to_have_url(build_url(BASE_URL, HomePage.PATH))
    expect(home_page.slider).to_be_visible()


def test_navigate_to_signup_login_page(home_page: HomePage) -> None:
    signup_login_page = home_page.header.go_to_signup_login_page()

    expect(signup_login_page.page).to_have_url(
        build_url(BASE_URL, SignupAndLoginPage.PATH)
    )
    expect.soft(signup_login_page.login_form_title).to_be_visible()
    expect.soft(signup_login_page.signup_form_title).to_be_visible()


def test_navigate_to_products_page_from_home(home_page: HomePage) -> None:
    products_page = home_page.header.go_to_products_page()

    expect(products_page.page).to_have_url(build_url(BASE_URL, ProductsPage.PATH))
    expect(products_page.product_listing.title).to_be_visible()
    expect(products_page.product_listing.title).to_have_text("All Products")
