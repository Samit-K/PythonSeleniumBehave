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


def before_scenario(context, scenario):

    browser_name = ConfigReader.read_configuration("basic info", "browser")
    options_to_add = ConfigReader.read_configuration("basic info", "options").split(', ')
    options = Options()
    if options_to_add:
        for option in options_to_add:
            options.add_argument(option)
    if browser_name.lower() == 'chrome':
        context.driver = webdriver.Chrome(options=options)
    elif browser_name.lower() == 'firefox':
        context.driver = webdriver.Firefox()
    elif browser_name.lower() == 'edge':
        context.driver = webdriver.Edge()

    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.get(ConfigReader.read_configuration("basic info", "url"))
    context.home_page = HomePage(context.driver)
    context.login_page = LoginPage(context.driver)
    context.cart_page = CartPage(context.driver)
    context.checkout_page = CheckoutPage(context.driver)
    context.base_page = BasePage(context.driver)


def after_scenario(context, scenario):
    context.driver.quit()


def after_step(context, step):
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(),
                      name="Fail_Screenshot",
                      attachment_type=AttachmentType.PNG)
