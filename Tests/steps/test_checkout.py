from Pages.login_page import LoginPage
from Pages.inventory_page import InventoryPage
from Pages.cart_page import CartPage
from Pages.checkout_page import CheckoutPage
from dotenv import load_dotenv
import os

load_dotenv(override=True)
USERNAME = os.getenv("SAUCE_USERNAME")
PASSWORD = os.getenv("SAUCE_PASSWORD")

def test_checkout_process(browser_page):
    # Login
    login = LoginPage(browser_page)
    login.load()
    login.login(USERNAME, PASSWORD)

    # Add item to cart
    inventory = InventoryPage(browser_page)
    inventory.add_to_cart()
    inventory.go_to_cart()

    # Go to checkout
    cart = CartPage(browser_page)
    cart.proceed_to_checkout()

    # Fill checkout info
    checkout = CheckoutPage(browser_page)
    checkout.fill_checkout_info("Prakash", "N", "11300")
    checkout.finish_order()

    # Verify success
    assert "Thank you for your order!" in checkout.get_success_message()
