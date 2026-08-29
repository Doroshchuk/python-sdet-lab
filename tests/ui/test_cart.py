from playwright.sync_api import Page, expect

from framework.pages.home_page import HomePage


# Test Case 12
def test_add_two_products_to_cart(page: Page) -> None:
    home_page = HomePage(page)
    home_page.open()
    products_page = home_page.go_to_products_page()
    first_product = products_page.product_at(0)
    first_product_info = first_product.product_info()
    first_product.add_to_cart().continue_shopping()
    second_product = products_page.product_at(1)
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
