from pages.BasePage import BasePage


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    item_quantity_xpath = "//input[contains(@name,'quantity')]"
    table_rows_xpath = "//table[@class='table table-bordered']//tr"
    update_item_quantity_button_xpath = "//button[@data-original-title='Update']"
    remove_item_xpath = "//button[@data-original-title='Remove']"
    page_title_xpath = "//*[@id='content']/h1"
    unit_price_xpath = "//*[@id='content']//tbody//td[5]"
    final_price_xpath = "//*[@id='content']//tbody//td[6]"

    def check_cart_page_title(self, expected_title):
        return self.get_element_text_contains("page_title_xpath", self.page_title_xpath, expected_title)

    def change_item_quantity(self, quantity):
        self.enter_into_element("item_quantity_xpath", self.item_quantity_xpath, quantity)

    def click_on_update(self):
        self.click_on_element("update_item_quantity_button_xpath", self.update_item_quantity_button_xpath)

    def click_on_remove_button(self):
        self.click_on_element("remove_item_xpath", self.remove_item_xpath)

    def extract_number_of_items_in_cart(self):
        number_of_rows = len(self.get_elements("table_rows_xpath", self.table_rows_xpath))
        return number_of_rows

    def remove_all_items(self):
        while self.extract_number_of_items_in_cart() > 0:
            self.click_on_remove_button()

    def get_unit_price(self):
        return self.get_element("unit_price_xpath", self.unit_price_xpath).text

    def final_price_check(self, expected_final_price):
        return self.get_element_number_contains("final_price_xpath", self.final_price_xpath, expected_final_price)




