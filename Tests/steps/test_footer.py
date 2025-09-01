def test_footer_text(page):
    page.goto("https://www.saucedemo.com/")
    footer_text = page.locator("div.footer_copy").text_content()
    assert "Sauce Labs" in footer_text