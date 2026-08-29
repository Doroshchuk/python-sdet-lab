from playwright.sync_api import Page

from framework.pages.base_page import BasePage
from framework.pages.components.cart_item import CartItem


class CartPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.cart_items = self.page.locator("#cart_info_table tbody").get_by_role("row")

    def cart_item_at(self, index: int) -> CartItem:
        return CartItem(self.cart_items.nth(index))
