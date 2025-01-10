from behave import *


@then(u'I navigated to the "{page_name}" Page')
@given(u'I navigated to the "{page_name}" Page')
def step_impl(context, page_name):
    if page_name.__contains__("Login"):
        assert context.login_page.display_status("login_button_id", "login-button")
    else:
        assert context.base_page.get_element_text_contains("page_title_class_name", "title", page_name)


@then(u'I see the title as "Swag Labs"')
def step_impl(context):
    assert context.login_page.verify_page_title("Swag Labs")


@when(u'I click the {button_name} button')
def step_impl(context, button_name):
    if button_name.__contains__("Login"):
        context.login_page.click_on_login_button()
    elif button_name.__contains__("Add to cart"):
        context.home_page.click_on_add_to_cart_from_inventory_page()
    elif button_name.__contains__("Checkout"):
        context.cart_page.click_on_checkout_button()
    elif button_name.__contains__("Continue"):
        context.checkout_page.click_on_continue_button()


@then(u'I see the "{field_name}" field')
def step_impl(context, field_name):
    if field_name.__contains__("Username"):
        assert context.login_page.display_status("username_field_id", context.login_page.username_field_id)
    elif field_name.__contains__("Password"):
        assert context.login_page.display_status("password_field_id", context.login_page.password_field_id)
    elif field_name.__contains__("First Name") or field_name.__contains__("Last Name") or field_name.__contains__("Postal Code"):
        assert context.checkout_page.display_status("field_name_xpath",
                                                    context.checkout_page.field_name_xpath.replace("[FIELD_NAME]", field_name))


@then(u'I see the "{button_name}" button')
def step_impl(context, button_name):
    if button_name.__contains__("Login"):
        assert context.login_page.display_status("login_button_id",
                                                 context.login_page.login_button_id)
    elif button_name.__contains__("Add to cart"):
        pass
    elif button_name.__contains__("Checkout"):
        pass
    elif button_name.__contains__("Continue"):
        pass


@when(u'I enter "{field_name}" as "{data}"')
def step_impl(context, field_name, data):
    if field_name == "Username":
        context.login_page.enter_username(data)
    elif field_name == "Password":
        context.login_page.enter_password(data)
    elif field_name == "First Name":
        context.checkout_page.enter_first_name(data)
    elif field_name == "Last Name":
        context.checkout_page.enter_last_name(data)
    elif field_name == "Zip/Postal Code":
        context.checkout_page.enter_zip_postal_code(data)


@then(u'I get logged in')
def step_impl(context):
    assert context.home_page.verify_page_title("Swag Labs")


@then(u'I get proper error message for "{error_message}"')
def step_impl(context, error_message):
    if error_message == "locked_out_user":
        expected_warning = "Sorry, this user has been locked out."
        assert context.login_page.warning_message_displayed(expected_warning)
    elif error_message == "empty credentials" or error_message == "no username":
        expected_warning = "Username is required"
        assert context.login_page.warning_message_displayed(expected_warning)
    elif error_message == "no password":
        expected_warning = "Password is required"
        assert context.login_page.warning_message_displayed(expected_warning)
    elif error_message == "wrong credentials":
        expected_warning = "Username and password do not match any user in this service"
        assert context.login_page.warning_message_displayed(expected_warning)
