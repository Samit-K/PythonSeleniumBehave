from pages.BasePage import BasePage


class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Locator constants for elements on the checkout page
    page_title_class_name = "title"
    field_name_xpath = "//input[contains(@placeholder,'[FIELD_NAME]')]"
    continue_button_id = "continue"
    products_subtotal_price_class_name = "summary_subtotal_label"
    product_tax_class_name = "summary_tax_label"
    products_total_price_class_name = "summary_total_label"

    # Enters the first name into the respective field
    def enter_first_name(self, first_name):
        self.enter_into_element("field_name_xpath",
                                self.field_name_xpath.replace("[FIELD_NAME]", "First Name"),
                                first_name)

    # Enters the last name into the respective field
    def enter_last_name(self, last_name):
        self.enter_into_element("field_name_xpath",
                                self.field_name_xpath.replace("[FIELD_NAME]", "Last Name"),
                                last_name)

    # Enters the zip/postal code into the respective field
    def enter_zip_postal_code(self, zip_postal_code):
        self.enter_into_element("field_name_xpath",
                                self.field_name_xpath.replace("[FIELD_NAME]", "Zip/Postal Code"),
                                zip_postal_code)

    # Clicks the continue button to proceed with the checkout
    def click_on_continue_button(self):
        self.click_on_element("continue_button_id", self.continue_button_id)
