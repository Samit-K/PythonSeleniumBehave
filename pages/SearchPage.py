from pages.BasePage import BasePage


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    valid_product_partial_link_text = "HP"
    err_message_xpath = "//p[contains(text(),'no product')]"

    def display_status_of_product(self):
        self.display_status("valid_product_partial_link_text", self.valid_product_partial_link_text)

    def check_error_message(self, err_message):
        self.get_element_text_equals("err_message_xpath", self.err_message_xpath, err_message)
