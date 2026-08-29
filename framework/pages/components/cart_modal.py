from playwright.sync_api import Page

from framework.pages.cart_page import CartPage


class CartModal:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.container = self.page.locator("#cartModal")
        self.continue_shopping_button = self.container.get_by_role(
            "button", name="Continue Shopping"
        )
        self.view_cart_link = self.container.get_by_role("link", name="View Cart")

    def continue_shopping(self) -> None:
        self.continue_shopping_button.click()

    def view_cart(self) -> CartPage:
        self.view_cart_link.click()
        return CartPage(self.page)
