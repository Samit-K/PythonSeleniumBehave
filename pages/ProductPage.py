import time

from pages.BasePage import BasePage


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    quantity_name = "quantity"
    add_to_cart_button_id = "button-cart"
    success_message_xpath = "//div[contains(text(),'Success')]"
    add_to_wishlist_button_xpath = "//button[contains(@onclick,'wishlist')]"
    add_item_for_compare_xpath = "//button[contains(@onclick,'compare')]"
    product_name_xpath = "//*[@id='content']//h1"
    small_radio_button_xpath = "//div[@class='radio']/label/input"
    checkbox_3_xpath = "(//div[@class='checkbox']/label/input)[2]"
    checkbox_4_xpath = "(//div[@class='checkbox']/label/input)[1]"
    text_area_1_id = "input-option208"
    drop_down_id = "input-option217"
    textarea_id = "input-option209"

    def get_product_name(self):
        return self.get_element("product_name_xpath", self.product_name_xpath).text

    def enter_quantity(self, quantity):
        self.enter_into_element("quantity_name", self.quantity_name, quantity)

    def click_on_add_to_cart_button(self):
        self.click_on_element("add_to_cart_button_id", self.add_to_cart_button_id)

    def add_item_to_wishlist(self):
        self.click_on_element("add_to_wishlist_button_xpath", self.add_to_wishlist_button_xpath)

    def add_item_to_compare(self):
        self.click_on_element("add_item_for_compare_xpath", self.add_item_for_compare_xpath)

    def check_success_message(self, success_message):
        time.sleep(3)
        return self.get_element_text_contains("success_message_xpath", self.success_message_xpath,
                                              success_message)
