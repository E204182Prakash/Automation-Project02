class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.first_name = "input[data-test='firstName']"
        self.last_name = "input[data-test='lastName']"
        self.postal_code = "input[data-test='postalCode']"
        self.continue_button = "input[data-test='continue']"
        self.finish_button = "button[data-test='finish']"
        self.success_message = ".complete-header"

    def fill_checkout_info(self, fname, lname, zipcode):
        self.page.fill(self.first_name, fname)
        self.page.fill(self.last_name, lname)
        self.page.fill(self.postal_code, zipcode)
        self.page.click(self.continue_button)

    def finish_order(self):
        self.page.click(self.finish_button)

    def get_success_message(self):
        return self.page.text_content(self.success_message)
