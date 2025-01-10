from selenium.webdriver.common.by import By

from utilities.NumberExtractor import extract_number_from_string


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_elements(self, locator_type, locator_value):
        elements = None
        if locator_type.endswith("_id"):
            elements = self.driver.find_element(By.ID, locator_value)
        elif locator_type.endswith("_name"):
            elements = self.driver.find_element(By.NAME, locator_value)
        elif locator_type.endswith("_class_name"):
            elements = self.driver.find_element(By.CLASS_NAME, locator_value)
        elif locator_type.endswith("_partial_link_text"):
            elements = self.driver.find_element(By.PARTIAL_LINK_TEXT, locator_value)
        elif locator_type.endswith("_link_text"):
            elements = self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_type.endswith("_xpath"):
            elements = self.driver.find_element(By.XPATH, locator_value)
        elif locator_type.endswith("_css"):
            elements = self.driver.find_element(By.CSS_SELECTOR, locator_value)
        else:
            print("No elements found")
        return elements if elements is not None else []

    def get_element(self, locator_type, locator_value):
        element = None
        if locator_type.endswith("_id"):
            element = self.driver.find_element(By.ID, locator_value)
        elif locator_type.endswith("_class_name"):
            element = self.driver.find_element(By.CLASS_NAME, locator_value)
        elif locator_type.endswith("_name"):
            element = self.driver.find_element(By.NAME, locator_value)
        elif locator_type.endswith("_partial_link_text"):
            element = self.driver.find_element(By.PARTIAL_LINK_TEXT, locator_value)
        elif locator_type.endswith("_link_text"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_type.endswith("_xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)
        elif locator_type.endswith("_css"):
            element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
        else:
            print(f"Invalid locator type: {locator_type}")
        return element

    def click_on_element(self, locator_type, locator_value):
        element = self.get_element(locator_type, locator_value)
        element.click()

    def display_status(self, locator_type, locator_value):
        element = self.get_element(locator_type, locator_value)
        return element.is_displayed()

    def verify_page_title(self, expected_title):
        return self.driver.title.__eq__(expected_title)

    def enter_into_element(self, locator_type, locator_value, text_to_be_entered):
        element = self.get_element(locator_type, locator_value)
        element.click()
        element.clear()
        element.send_keys(text_to_be_entered)

    def get_element_text_contains(self, locator_type, locator_value, expected_text):
        element = self.get_element(locator_type, locator_value)
        return element.text.__contains__(expected_text)

    def get_element_number_contains(self, locator_type, locator_value, expected_number):
        element = self.get_element(locator_type, locator_value)
        number = extract_number_from_string(element.text)
        print(number, expected_number)
        return number.__contains__(expected_number)

    def get_element_text_equals(self, locator_type, locator_value, expected_text):
        element = self.get_element(locator_type, locator_value)
        return element.text.__eq__(expected_text)
