from random import randint

from pages.BasePage import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    shopping_cart_class_name = "shopping_cart_link"
    side_menu_button_xpath = "//button[text()='Open Menu']"
    side_menu_item_xpath = "//a[text()='[MENU_ITEM]']"
    inventory_list_class_name = "inventory_list"
    inventory_item_name_xpath = "//div[@data-test='inventory-item-name' and text()='[PRODUCT_NAME]']"
    inventory_item_description_xpath = "inventory_item_description"
    inventory_item_pricebar_add_to_cart_button_class_name = "//div[@class='pricebar']/button"
    inventory_item_price_class_name = "inventory_item_price"
    product_sort_class_name = "product_sort_container"

    def click_on_shopping_cart(self):
        self.click_on_element("shopping_cart_class_name", self.shopping_cart_class_name)

    def click_on_side_menu_item(self, item):
        self.click_on_element("side_menu_item_xpath", self.side_menu_item_xpath.replace("[MENU_ITEM]", item))

    def click_on_item(self, product_name):
        self.click_on_element("inventory_item_name_xpath", self.inventory_item_name_xpath.replace("[PRODUCT_NAME]", product_name))

    def click_on_add_to_cart_from_inventory_page(self):
        self.click_on_element("inventory_item_pricebar_add_to_cart_button_class_name", self.inventory_item_pricebar_add_to_cart_button_class_name)

    def check_home_page_title(self, expected_title):
        return self.verify_page_title(expected_title)









    click_on_item("sauce labs")