from Pages.login_page import LoginPage
from Pages.inventory_page import InventoryPage

def test_valid_login(browser_page):
    login = LoginPage(browser_page)
    login.load()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(browser_page)
    assert inventory.is_loaded()

def test_invalid_login(browser_page):
    login = LoginPage(browser_page)
    login.load()
    login.login("wrong_user", "wrong_pass")
    assert "Epic sadface" in login.get_error_message()
