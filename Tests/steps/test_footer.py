from pytest_bdd import scenarios, given, then
from playwright.sync_api import Page, expect

scenarios("../features/footer.feature")


@given("I am on the login page")
def open_login_page(page: Page):
    page.goto("https://www.saucedemo.com/")


@then('I should see "Sauce Labs" in the footer')
def verify_footer(page: Page):
    footer_text = page.locator("div.footer_copy").text_content()
    assert "Sauce Labs" in footer_text
