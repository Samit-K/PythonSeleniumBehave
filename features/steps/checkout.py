from behave import *


@then(u'The "Item Total" on the "Checkout: Overview" page matches the total calculated on the "Your Cart" page')
def step_impl(context):
    assert context.checkout_page.get_element_text_contains("products_subtotal_price_class_name",
                                                           context.checkout_page.products_subtotal_price_class_name, "39.98")
