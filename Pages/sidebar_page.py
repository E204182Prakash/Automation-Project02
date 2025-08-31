class SidebarPage:
    def __init__(self, page):
        self.page = page
        self.menu_button = "button#react-burger-menu-btn"
        self.close_button = "button#react-burger-cross-btn"
        self.about_link = "a#about_sidebar_link"
        self.logout_link = "a#logout_sidebar_link"

    def open_sidebar(self):
        # If already open, close it first
        if self.page.is_visible(self.close_button):
            self.page.click(self.close_button)
        self.page.click(self.menu_button)

    def click_about(self):
        self.open_sidebar()
        self.page.click(self.about_link)

    def click_logout(self):
        self.open_sidebar()
        self.page.click(self.logout_link)
