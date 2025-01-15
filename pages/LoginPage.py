from pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        # Initialize the LoginPage object with the driver
        super().__init__(driver)

    # Define element locators
    username_field_id = "user-name"
    password_field_id = "password"
    login_button_id = "login-button"
    warning_xpath = "//h3[@data-test='error']"

    # Enters the username into the username field
    def enter_username(self, username):
        self.enter_into_element("username_field_id", self.username_field_id, username)

    # Enters the password into the password field
    def enter_password(self, password):
        self.enter_into_element("password_field_id", self.password_field_id, password)

    # Clicks on the login button to submit the login form
    def click_on_login_button(self):
        self.click_on_element("login_button_id", self.login_button_id)

    # Verifies if the expected warning message is displayed
    def warning_message_displayed(self, expected_warning):
        return self.get_element_text_contains("warning_xpath", self.warning_xpath, expected_warning)
