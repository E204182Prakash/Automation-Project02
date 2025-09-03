from playwright.sync_api import Page, expect

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_icon = page.locator(".shopping_cart_link")
        self.cart_items = page.locator(".cart_item")
        self.checkout_button = "button[data-test='checkout']"
        self.remove_button = page.locator("button[id^='remove']")

    def has_items(self):
        return self.cart_items.count() > 0

    def proceed_to_checkout(self):
        self.page.click(self.checkout_button)
    
    def open_cart(self):
        self.cart_icon.click()
        expect(self.page.locator(".cart_list")).to_be_visible()

    def remove_item(self):
        expect(self.remove_button.first).to_be_visible()
        self.remove_button.first.click()

    def is_cart_empty(self):
        return self.cart_items.count() == 0
    
    def is_checkout_page_displayed(self):
        return self.page.url.endswith("/checkout-step-one.html")