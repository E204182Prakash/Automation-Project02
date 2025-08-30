from Pages.login_page import LoginPage
from Pages.inventory_page import InventoryPage
from Pages.cart_page import CartPage
from dotenv import load_dotenv
import os

load_dotenv(override=True)
USERNAME = os.getenv("SAUCE_USERNAME")
PASSWORD = os.getenv("SAUCE_PASSWORD")

def test_add_to_cart(browser_page):
    login = LoginPage(browser_page)
    login.load()
    login.login(USERNAME, PASSWORD)

    inventory = InventoryPage(browser_page)
    inventory.add_to_cart()
    inventory.go_to_cart()

    cart = CartPage(browser_page)
    assert cart.has_items()
