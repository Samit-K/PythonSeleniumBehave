from pages.BasePage import BasePage


class RegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    first_name_id = "input-firstname"
    last_name_id = "input-lastname"
    email_id = "input-email"
    telephone_id = "input-telephone"
    password_id = "input-password"
    confirm_password_id = "input-confirm"
    privacy_policy_name = "agree"
    subscribe_yes_xpath = "//label[text()='Yes']/input"
    subscribe_no_xpath = "//label[text()='No']/input"
    continue_button_xpath = "//input[@value='Continue']"
    warning_message_xpath = "//div[@id='account-register']/div[1]"
    first_name_error_xpath = "//input[@id='input-firstname']/following-sibling::div"
    last_name_error_xpath = "//input[@id='input-lastname']/following-sibling::div"
    email_id_error_xpath = "//input[@id='input-email']/following-sibling::div"
    telephone_error_xpath = "//input[@id='input-telephone']/following-sibling::div"
    password_error_xpath = "//input[@id='input-password']/following-sibling::div"
    confirm_password_error_xpath = "//input[@id='input-confirm']/following-sibling::div"

    def enter_firstname(self, firstname):
        self.enter_into_element("first_name_id", self.first_name_id, firstname)

    def enter_lastname(self, lastname):
        self.enter_into_element("last_name_id", self.last_name_id, lastname)

    def enter_email(self, email):
        self.enter_into_element("email_id", self.email_id, email)

    def enter_telephone(self, telephone):
        self.enter_into_element("telephone_id", self.telephone_id, telephone)

    def enter_password(self, password):
        self.enter_into_element("password_id", self.password_id, password)

    def enter_confirm_password(self, confirm_password):
        self.enter_into_element("confirm_password_id", self.confirm_password_id, confirm_password)

    def click_on_privacy_policy(self):
        self.click_on_element("privacy_policy_name", self.privacy_policy_name)

    def click_on_yes_subscribe(self):
        self.click_on_element("subscribe_yes_xpath", self.subscribe_yes_xpath)

    def click_on_no_subscribe(self):
        self.click_on_element("subscribe_no_xpath", self.subscribe_no_xpath)

    def click_on_continue_button(self):
        self.click_on_element("continue_button_xpath", self.continue_button_xpath)

    def check_err_message(self, expected_warning):
        print(self.get_element("warning_message_xpath", self.warning_message_xpath).text)
        return self.get_element_text_contains("warning_message_xpath", self.warning_message_xpath, expected_warning)

    def check_confirm_password_error(self, confirm_error):
        return self.get_element_text_contains("confirm_password_error_xpath", self.confirm_password_error_xpath,
                                              confirm_error)

    def display_status_of_all_warning(self, expected_privacy_policy_warning, expected_firstname_warning,
                                      expected_lastname_warning, expected_email_warning, expected_telephone_warning,
                                      expected_password_warning):
        privacy_policy_status = self.get_element_text_contains("warning_message_xpath", self.warning_message_xpath,
                                                               expected_privacy_policy_warning)
        first_name_status = self.get_element_text_equals("first_name_error_xpath", self.first_name_error_xpath,
                                                         expected_firstname_warning)
        last_name_status = self.get_element_text_equals("last_name_error_xpath", self.last_name_error_xpath,
                                                        expected_lastname_warning)
        email_status = self.get_element_text_equals("email_id_error_xpath", self.email_id_error_xpath,
                                                    expected_email_warning)
        telephone_status = self.get_element_text_equals("telephone_error_xpath", self.telephone_error_xpath,
                                                        expected_telephone_warning)
        password_status = self.get_element_text_equals("password_error_xpath", self.password_error_xpath,
                                                       expected_password_warning)

        if privacy_policy_status and first_name_status and last_name_status and email_status and telephone_status and password_status:
            return True
        else:
            return False
