from pages.BasePage import BasePage


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Define element locators
    checkout_button_id = "checkout"

    # Click actions
    def click_on_checkout_button(self):
        self.click_on_element("checkout_button_id", self.checkout_button_id)
