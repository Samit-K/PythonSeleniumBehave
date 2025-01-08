import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
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
    context.driver.get(ConfigReader.read_configuration("basic info", "url"))


def after_scenario(context, scenario):
    context.driver.quit()


def after_step(context, step):
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(),
                      name="Fail_Screenshot",
                      attachment_type=AttachmentType.PNG)
