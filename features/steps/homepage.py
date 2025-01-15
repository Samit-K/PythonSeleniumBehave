from behave import *
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage

# Step implementation for checking if a specific element is displayed
@then(u'I see the "{element}"')
def step_impl(context, element):
    # Check for "Inventory List" visibility
    if "Inventory List" in element:
        assert context.home_page.display_status("inventory_list_class_name", context.home_page.inventory_list_class_name)
    # Check for "Inventory Items" visibility
    elif "Inventory Items" in element:
        assert context.home_page.display_status("inventory_item_class_name", context.home_page.inventory_item_class_name)

# Step implementation for checking if a specific icon is displayed
@then(u'I see the "{icon}" icon')
def step_impl(context, icon):
    # Check for Cart icon visibility
    if "Cart" in icon:
        assert context.home_page.display_status("shopping_cart_class_name", "shopping_cart_link")

# Step implementation for clicking a specific icon
@when(u'I click the "{icon}" icon')
def step_impl(context, icon):
    # Click on the Cart icon
    context.home_page.click_on_shopping_cart()

# Step implementation for clicking the "Add to cart" button for the first two products
@when(u'I click the "Add to cart" button for the first two products')
def step_impl(context):
    # Click "Add to Cart" for the first product
    context.home_page.click_on_element("inventory_item_pricebar_add_to_cart_button_xpath",
                                       "(//div[@class='pricebar']/button)[1]")
    # Click "Add to Cart" for the second product
    context.home_page.click_on_element("inventory_item_pricebar_add_to_cart_button_xpath",
                                       "(//div[@class='pricebar']/button)[2]")

# Step implementation for checking if the Cart icon displays the correct number of items
@then(u'I see the Cart icon display the number "{number}"')
def step_impl(context, number):
    # Verify that the Cart icon displays the expected number of items
    assert context.home_page.get_element_text_contains("cart_item_number_class_name", "shopping_cart_badge", number)
