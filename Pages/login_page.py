class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = "input[data-test='username']"
        self.password_input = "input[data-test='password']"
        self.login_button = "input[data-test='login-button']"
        self.error_message = "h3[data-test='error']"

    def load(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    def get_error_message(self):
        return self.page.text_content(self.error_message)
