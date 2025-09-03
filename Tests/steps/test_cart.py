from Pages.login_page import LoginPage
from Pages.inventory_page import InventoryPage
from Pages.cart_page import CartPage
from dotenv import load_dotenv
import os
import pytest
from pytest_bdd import scenarios, given, when, then

scenarios('../features/cart.feature')

load_dotenv(override=True)
USERNAME = os.getenv("SAUCE_USERNAME")
PASSWORD = os.getenv("SAUCE_PASSWORD")

@pytest.fixture
def login_page(browser_page):
    return LoginPage(browser_page)

@pytest.fixture
def inventory_page(browser_page):
    return InventoryPage(browser_page)

@pytest.fixture
def cart_page(browser_page):
    return CartPage(browser_page)


@given("I am logged in with valid credentials")
def step_login(login_page):
    login_page.load()
    login_page.login(USERNAME, PASSWORD)


@when("the user add a product to the cart")
def step_add_to_cart(inventory_page):
    inventory_page.add_to_cart()


@when("the user navigate to the cart page")
def step_go_to_cart(inventory_page):
    inventory_page.go_to_cart()


@then("the user should see the product in the cart")
def step_verify_cart(cart_page):
    assert cart_page.has_items(), "Cart is empty!"


@when("the user removes the item from the cart")
def step_remove_item(cart_page):
    cart_page.open_cart()
    cart_page.remove_item()


@then("the cart should be empty")
def step_cart_should_be_empty(cart_page):
    assert cart_page.is_cart_empty(), "Cart is not empty after removing item!"
