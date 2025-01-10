from behave import *

from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage


@then(u'I see the "{element}"')
def step_impl(context, element):
    if element.__contains__("Inventory List"):
        assert context.home_page.display_status("inventory_list_class_name", context.home_page.inventory_list_class_name)
    elif element.__contains__("Inventory Items"):
        assert context.home_page.display_status("inventory_item_class_name", context.home_page.inventory_item_class_name)


@then(u'I see the "{icon}" icon')
def step_impl(context, icon):
    if icon.__contains__("Cart"):
        assert context.home_page.display_status("shopping_cart_class_name", "shopping_cart_link")


@when(u'I click the "{icon}" icon')
def step_impl(context, icon):
    context.home_page.click_on_shopping_cart()


@when(u'I click the "Add to cart" button for the first two products')
def step_impl(context):
    context.home_page.click_on_element("inventory_item_pricebar_add_to_cart_button_xpath",
                                       "(//div[@class='pricebar']/button)[1]")
    context.home_page.click_on_element("inventory_item_pricebar_add_to_cart_button_xpath",
                                       "(//div[@class='pricebar']/button)[2]")


@then(u'I see the Cart icon display the number "{number}"')
def step_impl(context, number):
    assert context.home_page.get_element_text_contains("cart_item_number_class_name", "shopping_cart_badge", number)
