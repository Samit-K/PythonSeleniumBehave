from behave import *

from pages.AccountSuccessPage import AccountSuccessPage
from pages.HomePage import HomePage
from pages.RegisterPage import RegisterPage
from utilities import EmailWithTimeStampGenerator


@given(u'I navigate to Register page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account()
    context.home_page.select_register_option()


@when(u'I enter details into mandatory fields')
def step_impl(context):
    for row in context.table:
        new_email = EmailWithTimeStampGenerator.get_email_with_time_stamp()
        context.register_page = RegisterPage(context.driver)
        context.register_page.enter_firstname(row["first_name"])
        context.register_page.enter_lastname(row["last_name"])
        context.register_page.enter_email(new_email)
        context.register_page.enter_telephone(row["telephone"])


@when(u'I enter password in both password fields')
def step_impl(context):
    for row in context.table:
        context.register_page = RegisterPage(context.driver)
        context.register_page.enter_password(row["password"])
        context.register_page.enter_confirm_password(row["password"])


@when(u'I enter password in password field')
def step_impl(context):
    for row in context.table:
        context.register_page = RegisterPage(context.driver)
        context.register_page.enter_password(row["password"])


@when(u'I enter another password in confirm password field')
def step_impl(context):
    for row in context.table:
        context.register_page = RegisterPage(context.driver)
        context.register_page.enter_confirm_password(row["confirm_password"])


@when (u'I click on privacy policy')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.click_on_privacy_policy()


@when(u'I click on Continue button')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.click_on_continue_button()


@then(u'Account should get created')
def step_impl(context):
    success_message = "Your Account Has Been Created!"
    context.account_success_page = AccountSuccessPage(context.driver)
    context.account_success_page.check_account_created_message(success_message)


@when(u'I enter details in all fields')
def step_impl(context):
    for row in context.table:
        new_email = EmailWithTimeStampGenerator.get_email_with_time_stamp()
        context.register_page = RegisterPage(context.driver)
        context.register_page.enter_firstname(row["first_name"])
        context.register_page.enter_lastname(row["last_name"])
        context.register_page.enter_email(new_email)
        context.register_page.enter_telephone(row["telephone"])
        context.register_page.click_on_yes_subscribe()


@when(u'I enter details into all fields except email')
def step_impl(context):
    for row in context.table:
        context.register_page = RegisterPage(context.driver)
        context.register_page.enter_firstname(row["first_name"])
        context.register_page.enter_lastname(row["last_name"])
        context.register_page.enter_telephone(row["telephone"])
        context.register_page.click_on_yes_subscribe()


@when(u'I enter existing email address into the email field')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.enter_email("testuser123@gmail.com")


@then(u'Proper warning message should be displayed')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.check_err_message("Warning")


@then(u'Privacy Policy warning should be shown')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.check_err_message("Privacy Policy")


@then(u'Password mismatch error should be displayed')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    err_message = "Password confirmation does not match password!"
    context.register_page.check_confirm_password_error(err_message)


@when(u'I dont enter details into any field')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.enter_firstname("")
    context.register_page.enter_lastname("")
    context.register_page.enter_email("")
    context.register_page.enter_telephone("")


@then(u'Proper warning message for all mandatory fields should be displayed')
def step_impl(context):
    expected_privacy_policy_warning = "Warning: You must agree to the Privacy Policy!"
    expected_first_name_warning = "First Name must be between 1 and 32 characters!"
    expected_last_name_warning = "Last Name must be between 1 and 32 characters!"
    expected_email_warning = "E-Mail Address does not appear to be valid!"
    expected_telephone_warning = "Telephone must be between 3 and 32 characters!"
    expected_password_warning = "Password must be between 4 and 20 characters!"
    context.register_page = RegisterPage(context.driver)
    context.register_page.display_status_of_all_warning(expected_privacy_policy_warning,
                                                        expected_first_name_warning,
                                                        expected_last_name_warning,
                                                        expected_email_warning,
                                                        expected_telephone_warning,
                                                        expected_password_warning)
