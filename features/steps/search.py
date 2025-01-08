import time

from behave import *

from pages.HomePage import HomePage
from pages.SearchPage import SearchPage


@given(u'I got navigated to home page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    expected_title = "Your Store"
    assert context.home_page.check_home_page_title(expected_title)


@when(u'I enter valid product name "{product}" into the Search box')
def step_impl(context, product):
    context.home_page = HomePage(context.driver)
    context.home_page.search_item(product)


@when(u'I click on Search button')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_search_button()


@then(u'Valid product should get displayed in Search results')
def step_impl(context):
    context.search_page = SearchPage(context.driver)
    context.search_page.display_status_of_product()


@when(u'I enter invalid product name "{product}" into the Search box')
def step_impl(context, product):
    context.home_page = HomePage(context.driver)
    context.home_page.search_item(product)


@then(u'Proper message should be displayed in Search results')
def step_impl(context):
    expected_text = "There is no product that matches the search criteria."
    context.search_page = SearchPage(context.driver)
    context.search_page.check_error_message(expected_text)


@when(u'I dont enter anything into the Search box')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.search_item('')

