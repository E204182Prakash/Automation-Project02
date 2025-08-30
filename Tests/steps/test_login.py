import os
import pytest
from pytest_bdd import scenarios, given, when, then
from Pages.login_page import LoginPage
from Pages.inventory_page import InventoryPage
from dotenv import load_dotenv

# Load .env
load_dotenv(override=True)

# Link feature file
scenarios('../features/login.feature')

@pytest.fixture
def login_page(browser_page):
    return LoginPage(browser_page)

@pytest.fixture
def inventory_page(browser_page):
    return InventoryPage(browser_page)

@given("I am on the login page")
def open_login_page(login_page):
    login_page.load()

@when("the user enter valid username and password")
def enter_valid_credentials(login_page):
    login_page.login(os.getenv("SAUCE_USERNAME"), os.getenv("SAUCE_PASSWORD"))

@when("the user enter invalid username and password")
def enter_invalid_credentials(login_page):
    login_page.login("wrong_user", "wrong_pass")

@when("the user click the login button")
def click_login_button():
    pass

@then("the user should see the inventory page")
def verify_inventory_page(inventory_page):
    assert inventory_page.is_loaded(), "Inventory page did not load"

@then("the user should see an error message")
def verify_error_message(login_page):
    assert "Epic sadface" in login_page.get_error_message()
