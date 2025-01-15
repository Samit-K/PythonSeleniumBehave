import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from pages.BasePage import BasePage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from utilities import ConfigReader
from selenium.webdriver.chrome.options import Options


# This function sets up the browser and initializes page objects before each scenario
def before_scenario(context, scenario):
    # Get browser name and options from configuration
    browser_name = ConfigReader.read_configuration("basic info", "browser")
    options_to_add = ConfigReader.read_configuration("basic info", "options").split(', ')
    options = Options()

    # Add any specified options to the browser
    if options_to_add:
        for option in options_to_add:
            options.add_argument(option)

    # Initialize the appropriate browser based on the configuration
    if browser_name.lower() == 'chrome':
        context.driver = webdriver.Chrome(options=options)
    elif browser_name.lower() == 'firefox':
        context.driver = webdriver.Firefox(options=options)
    elif browser_name.lower() == 'edge':
        context.driver = webdriver.Edge(options=options)

    # Maximize the browser window and set implicit wait time
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)

    # Navigate to the base URL
    context.driver.get(ConfigReader.read_configuration("basic info", "url"))

    # Initialize page objects for later use in the tests
    context.home_page = HomePage(context.driver)
    context.login_page = LoginPage(context.driver)
    context.cart_page = CartPage(context.driver)
    context.checkout_page = CheckoutPage(context.driver)
    context.base_page = BasePage(context.driver)


# This function is executed after each scenario, quitting the browser
def after_scenario(context, scenario):
    context.driver.quit()


# This function captures a screenshot after a failed step
def after_step(context, step):
    if step.status == 'failed':
        # Attach a screenshot to the allure report
        allure.attach(context.driver.get_screenshot_as_png(),
                      name="Fail_Screenshot",
                      attachment_type=AttachmentType.PNG)
