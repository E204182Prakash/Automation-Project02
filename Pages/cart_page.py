class CartPage:
    def __init__(self, page):
        self.page = page
        self.cart_item = ".cart_item"
        self.checkout_button = "button[data-test='checkout']"

    def has_items(self):
        return self.page.is_visible(self.cart_item)

    def proceed_to_checkout(self):
        self.page.click(self.checkout_button)
