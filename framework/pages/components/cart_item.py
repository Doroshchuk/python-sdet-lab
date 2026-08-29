from playwright.sync_api import Locator


class CartItem:
    def __init__(self, container: Locator) -> None:
        self.container = container

        self.title = self.container.locator(".cart_description").get_by_role("heading")
        self.price = self.container.locator(".cart_price p")
        self.quantity = self.container.locator(".cart_quantity").get_by_role("button")
        self.total_price = self.container.locator(".cart_total p")
