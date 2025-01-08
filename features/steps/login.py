from behave import *

from pages.AccountPage import AccountPage
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from utilities import EmailWithTimeStampGenerator


@given(u'I navigated to login page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account()
    context.home_page.select_login_option()


@when(u'I entered valid email address as "{email}" and valid password as "{password}" into the fields')
def step_impl(context, email, password):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email(email)
    context.login_page.enter_password(password)


@when(u'I click on Login button')
def step_impl(context):
    context.login_page.click_on_login_button()


@then(u'I should get logged in')
def step_impl(context):
    account_page = AccountPage(context.driver)
    assert account_page.display_status_of_edit_your_account_link_text()


@when(u'I entered invalid email address and valid password as "{password}" into the fields')
def step_impl(context, password):
    invalid_email = EmailWithTimeStampGenerator.get_email_with_time_stamp()
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email(invalid_email)
    context.login_page.enter_password(password)


@then(u'I should get proper warning message')
def step_impl(context):
    expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
    assert context.login_page.warning_message_displayed(expected_warning_message)


@when(u'I entered valid email address as "{email}" and invalid password as "{inv_password}" into the fields')
def step_impl(context, email, inv_password):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email(email)
    context.login_page.enter_password(inv_password)


@when(u'I entered invalid email address and invalid password as "{inv_password}" into the fields')
def step_impl(context, inv_password):
    invalid_email = EmailWithTimeStampGenerator.get_email_with_time_stamp()
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email(invalid_email)
    context.login_page.enter_password(inv_password)


@when(u'I do not enter anything into the email and password fields')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email("")
    context.login_page.enter_password("")
