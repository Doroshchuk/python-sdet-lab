from dataclasses import dataclass

from playwright.sync_api import Locator, Page

from framework.pages.components.cart_modal import CartModal
from framework.pages.product_details_page import ProductDetailsPage


@dataclass(frozen=True)
class ProductInfo:
    title: str
    price: str


class ProductCard:
    def __init__(self, page: Page, card: Locator) -> None:
        self.page = page
        # product
        self.card = card
        self.product_info_container = self.card.locator(".productinfo")
        self.title = self.product_info_container.locator("p")
        self.price = self.product_info_container.get_by_role("heading")
        self.view_product_link = self.card.locator(".choose a")
        self.image = self.product_info_container.get_by_role("img")

        # overlay
        self.overlay = self.card.locator(".product-overlay")
        self.overlay_add_to_cart_button = self.overlay.locator("a.add-to-cart")

    def product_info(self) -> ProductInfo:
        return ProductInfo(title=self.title.inner_text(), price=self.price.inner_text())

    def wait_for_image_to_load(self) -> None:
        self.image.wait_for_function("(img) => img.complete && img.naturalHeight > 0")

    def add_to_cart(self) -> CartModal:
        self.card.hover()
        self.overlay_add_to_cart_button.click()
        return CartModal(self.page)

    def view_product(self) -> ProductDetailsPage:
        self.view_product_link.click()
        return ProductDetailsPage(self.page)
