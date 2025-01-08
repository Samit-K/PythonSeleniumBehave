from pages.BasePage import BasePage


class AccountSuccessPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    account_created_confirmation_xpath = "//h1[contains(text(),'Created')]"

    def check_account_created_message(self, success_message):
        self.get_element_text_equals("account_created_confirmation_xpath", self.account_created_confirmation_xpath, success_message)