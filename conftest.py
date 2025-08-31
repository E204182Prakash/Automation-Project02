import pytest
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv

# Load .env once for the whole test run
load_dotenv(override=True)

@pytest.fixture(scope="function")
def browser_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        yield page
        browser.close()
