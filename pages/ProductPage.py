from pages.BasePage import BasePage


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)  # Initialize parent class with WebDriver

    # Define element locators
    add_to_cart_button_id = "add-to-cart"
    remove_from_cart_button_id = "remove"
    product_name_xpath = "//div[@data-test='inventory-item-name']"
    product_description_xpath = "//div[@data-test='inventory-item-desc']"
    product_price_xpath = "//div[@data-test='inventory-item-price']"

    # Get product details
    def get_product_name(self):
        return self.get_element("product_name_xpath", self.product_name_xpath).text

    def get_product_price(self):
        return self.get_element("product_price_xpath", self.product_price_xpath).text

    def get_product_description(self):
        return self.get_element("product_description_xpath", self.product_description_xpath).text

    # Click actions
    def click_on_add_to_cart_button(self):
        self.click_on_element("add_to_cart_button_id", self.add_to_cart_button_id)

    def click_on_remove_from_cart_button(self):
        self.click_on_element("remove_from_cart_button_id", self.remove_from_cart_button_id)
