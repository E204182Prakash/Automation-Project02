from Pages.login_page import LoginPage
from Pages.inventory_page import InventoryPage
from Pages.sidebar_page import SidebarPage
from dotenv import load_dotenv
import os
import pytest
from pytest_bdd import scenarios, given, when, then

scenarios('../features/sidebar.feature')

load_dotenv(override=True)
USERNAME = os.getenv("SAUCE_USERNAME")
PASSWORD = os.getenv("SAUCE_PASSWORD")

@pytest.fixture
def login_page(browser_page):
    return LoginPage(browser_page)

@pytest.fixture
def sidebar_page(browser_page):
    return SidebarPage(browser_page)


@given("I am logged in with valid credentials")
def step_login(login_page):
    login_page.load()
    login_page.login(USERNAME, PASSWORD)


@when("the user open the sidebar")
def step_open_sidebar(sidebar_page):
    sidebar_page.open_sidebar()


@when("the user click on About")
def step_click_about(sidebar_page):
    sidebar_page.click_about()


@then("the user should be redirected to the Sauce Labs About page")
def step_verify_about(browser_page):
    assert "saucelabs.com" in browser_page.url


@when("the user click on Logout")
def step_click_logout(sidebar_page):
    sidebar_page.click_logout()


@then("the user should be redirected back to the login page")
def step_verify_logout(browser_page):
    assert "saucedemo.com" in browser_page.url
    assert "login" in browser_page.url or browser_page.is_visible("input[data-test='login-button']")