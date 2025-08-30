from Pages.login_page import LoginPage
from Pages.inventory_page import InventoryPage
from Pages.cart_page import CartPage

def test_add_to_cart(browser_page):
    login = LoginPage(browser_page)
    login.load()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(browser_page)
    inventory.add_to_cart()
    inventory.go_to_cart()

    cart = CartPage(browser_page)
    assert cart.has_items()
