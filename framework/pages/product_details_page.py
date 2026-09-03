from playwright.sync_api import Page

from framework.pages.base_page import BasePage
from framework.pages.components.cart_modal import CartModal


class ProductDetailsPage(BasePage):
    PATH = "/product_details"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.product_details = self.page.locator(".product-details")
        self.title = self.product_details.get_by_role("heading")
        self.quantity_input = self.product_details.locator("#quantity")
        self.add_to_cart_button = self.product_details.get_by_role(
            "button", name="Add to cart"
        )

    def set_quantity(self, quantity: int) -> None:
        self.quantity_input.fill(str(quantity))

    def add_to_cart(self) -> CartModal:
        self.add_to_cart_button.click()
        return CartModal(self.page)
