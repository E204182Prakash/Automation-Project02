from Pages.login_page import LoginPage
from Pages.inventory_page import InventoryPage
from dotenv import load_dotenv
import os

# Load .env and override OS vars
load_dotenv(override=True)
USERNAME = os.getenv("SAUCE_USERNAME")
PASSWORD = os.getenv("SAUCE_PASSWORD")

def test_valid_login(browser_page):
    login = LoginPage(browser_page)
    login.load()
    login.login(USERNAME, PASSWORD)
    inventory = InventoryPage(browser_page)
    assert inventory.is_loaded(), "Inventory page did not load after login"
    print("successfull login")

def test_invalid_login(browser_page):
    login = LoginPage(browser_page)
    login.load()
    login.login("wrong_user", "wrong_pass")
    assert "Epic sadface" in login.get_error_message()
