from selenium.webdriver.common.by import By
from utilities.NumberExtractor import extract_number_from_string


class BasePage:

    def __init__(self, driver):
        # Initialize the driver for the page
        self.driver = driver

    # Returns a list of elements found by the given locator type and value
    def get_elements(self, locator_type, locator_value):
        elements = None
        # Identify the locator type and find the element accordingly
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

    # Returns a single element found by the given locator type and value
    def get_element(self, locator_type, locator_value):
        element = None
        # Identify the locator type and find the element accordingly
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

    # Clicks on an element identified by the given locator type and value
    def click_on_element(self, locator_type, locator_value):
        element = self.get_element(locator_type, locator_value)
        element.click()

    # Returns True if the element is displayed, False otherwise
    def display_status(self, locator_type, locator_value):
        element = self.get_element(locator_type, locator_value)
        return element.is_displayed()

    # Verifies if the page title matches the expected title
    def verify_page_title(self, expected_title):
        return self.driver.title == expected_title

    # Enters text into a field identified by the given locator type and value
    def enter_into_element(self, locator_type, locator_value, text_to_be_entered):
        element = self.get_element(locator_type, locator_value)
        element.click()
        element.clear()
        element.send_keys(text_to_be_entered)

    # Checks if the element's text contains the expected text
    def get_element_text_contains(self, locator_type, locator_value, expected_text):
        element = self.get_element(locator_type, locator_value)
        return expected_text in element.text

    # Checks if the element's text contains the expected number (using a utility to extract numbers)
    def get_element_number_contains(self, locator_type, locator_value, expected_number):
        element = self.get_element(locator_type, locator_value)
        number = extract_number_from_string(element.text)
        print(number, expected_number)
        return expected_number in number

    # Checks if the element's text exactly matches the expected text
    def get_element_text_equals(self, locator_type, locator_value, expected_text):
        element = self.get_element(locator_type, locator_value)
        return element.text == expected_text
