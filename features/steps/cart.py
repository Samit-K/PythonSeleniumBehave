from behave import *
from selenium.common import NoSuchElementException

from pages.CartPage import CartPage
from pages.HomePage import HomePage
from pages.ProductPage import ProductPage


@then(u'I see the "first two" products added to the cart')
def step_impl(context):
    pass
