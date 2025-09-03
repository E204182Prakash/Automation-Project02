class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.inventory_item = ".inventory_item"
        self.add_to_cart_button = (
            "button[data-test='add-to-cart-sauce-labs-bike-light']"
        )
        self.cart_icon = ".shopping_cart_link"

    def is_loaded(self):
        return self.page.is_visible(self.inventory_item)

    def add_to_cart(self):
        self.page.click(self.add_to_cart_button)

    def go_to_cart(self):
        self.page.click(self.cart_icon)
