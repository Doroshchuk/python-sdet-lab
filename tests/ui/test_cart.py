import re

from playwright.sync_api import Page, expect

from framework.config.settings import BASE_URL
from framework.pages.home_page import HomePage
from framework.utils.common import build_url


# Test Case 12
def test_add_two_products_to_cart(page: Page) -> None:
    home_page = HomePage(page)
    home_page.open()
    products_page = home_page.go_to_products_page()
    first_product = products_page.product_listing.product_at(0)
    first_product_info = first_product.product_info()
    first_product.add_to_cart().continue_shopping()
    second_product = products_page.product_listing.product_at(1)
    second_product_info = second_product.product_info()
    cart_page = second_product.add_to_cart().view_cart()

    expect(cart_page.cart_items).to_have_count(2)

    first_cart_item = cart_page.cart_item_at(0)
    second_cart_item = cart_page.cart_item_at(1)

    expect.soft(first_cart_item.title).to_have_text(first_product_info.title)
    expect.soft(first_cart_item.price).to_have_text(first_product_info.price)
    expect.soft(first_cart_item.quantity).to_have_text("1")
    expect.soft(first_cart_item.total_price).to_have_text(first_product_info.price)

    expect.soft(second_cart_item.title).to_have_text(second_product_info.title)
    expect.soft(second_cart_item.price).to_have_text(second_product_info.price)
    expect.soft(second_cart_item.quantity).to_have_text("1")
    expect.soft(second_cart_item.total_price).to_have_text(second_product_info.price)


# Test Case 13
def test_view_product_quantity_in_the_cart(page: Page) -> None:
    home_page = HomePage(page)
    home_page.open()
    first_product = home_page.product_listing.product_at(0)
    first_product_info = first_product.product_info()
    product_details_page = first_product.view_product()

    expect(product_details_page.page).to_have_url(
        re.compile(rf"{re.escape(build_url(BASE_URL, product_details_page.PATH))}/\d+$")
    )
    expect(product_details_page.title).to_have_text(first_product_info.title)

    expected_quantity = 4
    product_details_page.set_quantity(expected_quantity)
    cart_page = product_details_page.add_to_cart().view_cart()

    expect(cart_page.cart_items).to_have_count(1)
    cart_item = cart_page.cart_item_at(0)
    expect(cart_item.title).to_have_text(first_product_info.title)
    expect(cart_item.quantity).to_have_text(str(expected_quantity))
