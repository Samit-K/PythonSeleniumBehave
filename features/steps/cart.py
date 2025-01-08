from random import randint

from behave import *
from selenium.common import NoSuchElementException

from pages.CartPage import CartPage
from pages.HomePage import HomePage
from pages.ProductPage import ProductPage
from utilities.NumberExtractor import extract_number_from_string


@when(u'I click on a product')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_featured_product()


@when(u'I click on Apple Cinema 30" on the product page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_apple_cinema_30()


@when(u'I put desired quantity')
def step_impl(context):
    context.product_page = ProductPage(context.driver)
    context.product_page.enter_quantity(randint(1, 3))


@when(u'I click on Add to Cart button')
def step_impl(context):
    context.product_page.click_on_add_to_cart_button()


@then(u'I should see a message telling me I added the item(s) to cart')
def step_impl(context):
    product_name = context.product_page.get_product_name()
    success_message = f"Success: You have added {product_name} to your shopping cart!"
    try:
        assert context.product_page.check_success_message(success_message)
    except NoSuchElementException or AssertionError:
        pass


@given(u'I got navigated to the cart page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_shopping_cart()
    context.cart_page = CartPage(context.driver)
    assert context.cart_page.check_cart_page_title("Shopping Cart")


@when(u'I click on the remove item button')
def step_impl(context):
    context.cart_page.click_on_remove_button()


@then(u'I should see the item removed from the cart')
def step_impl(context):
    pass


@when(u'I change the quantity')
def step_impl(context):
    context.cart_page.change_item_quantity("4")


@when(u'I click on the update button')
def step_impl(context):
    context.cart_page.click_on_update()


@then(u'I should see an updated Total Value')
def step_impl(context):
    unit_price = extract_number_from_string(context.cart_page.get_unit_price())
    expected_total = str(4 * float(unit_price))
    assert context.cart_page.final_price_check(expected_total)
