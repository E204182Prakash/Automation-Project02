from Pages.login_page import LoginPage
from Pages.inventory_page import InventoryPage
from Pages.cart_page import CartPage
from Pages.checkout_page import CheckoutPage
from dotenv import load_dotenv
import os
import pytest
from pytest_bdd import scenarios, given, when, then

scenarios("../features/checkout.feature")


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


@pytest.fixture
def checkout_page(browser_page):
    return CheckoutPage(browser_page)


@given("I am logged in with valid credentials")
def step_login(login_page):
    login_page.load()
    login_page.login(USERNAME, PASSWORD)


@given("I have added a product to the cart")
def step_add_product(inventory_page):
    inventory_page.add_to_cart()
    inventory_page.go_to_cart()


@when("the user proceed to checkout")
def step_proceed_checkout(cart_page):
    cart_page.proceed_to_checkout()


@when("the user provide checkout information")
def step_fill_checkout(checkout_page):
    checkout_page.fill_checkout_info("Prakash", "N", "11300")


@when("the user finish the order")
def step_finish_order(checkout_page):
    checkout_page.finish_order()


@then("the user should see the success message")
def step_verify_success(checkout_page):
    assert "Thank you for your order!" in checkout_page.get_success_message()
