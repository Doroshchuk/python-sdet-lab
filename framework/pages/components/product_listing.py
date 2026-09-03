from playwright.sync_api import Page

from framework.pages.components.product_card import ProductCard


class ProductListing:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.container = self.page.locator(".features_items")
        self.title = self.container.locator("h2.title")
        self.product_cards = self.container.locator(".product-image-wrapper")

    def product_at(self, index: int) -> ProductCard:
        return ProductCard(self.page, self.product_cards.nth(index))

    def product_card(self, product_title: str) -> ProductCard:
        title = self.container.locator(".productinfo").get_by_text(
            product_title, exact=True
        )
        card = self.product_cards.filter(has=title)
        return ProductCard(self.page, card)

    def product_titles(self) -> list[str]:
        return self.product_cards.locator(".productinfo p").all_text_contents()
