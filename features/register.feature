Feature: Register Account functionality

  @register
  Scenario: Register with mandatory fields
    Given I navigate to Register page
    When I enter details into mandatory fields
      |first_name   |last_name   |telephone          |
      |Tester       |Testerz     |9123456789         |
    And I click on privacy policy
    And I enter password in both password fields
      |password           |
      |TesterPassword     |
    And I click on Continue button
    Then Account should get created

  @password
  Scenario: Register with different password and confirm password
    Given I navigate to Register page
    When I enter details into mandatory fields
      |first_name   |last_name   |telephone          |
      |Tester       |Testerz     |9123456789         |
    And I click on privacy policy
    And I enter password in password field
      |password           |
      |TesterPassword     |
    And I enter another password in confirm password field
      |confirm_password           |
      |NotTesterPassword          |
    And I click on Continue button
    Then Password mismatch error should be displayed

  @duplicate
  Scenario: Register with duplicate email address
    Given I navigate to Register page
    When I enter details into all fields except email
      |first_name   |last_name   |telephone          |
      |Tester       |Testerz     |9123456789         |
    And I click on privacy policy
    And I enter existing email address into the email field
    And I enter password in both password fields
      |password           |
      |TesterPassword     |
    And I click on Continue button
    Then Proper warning message should be displayed

  @empty
  Scenario: Register without providing any details
    Given I navigate to Register page
    When I dont enter details into any field
    And I click on Continue button
    Then Proper warning message for all mandatory fields should be displayed

  @privacy-policy
  Scenario: Register without clicking on Privacy Policy
    Given I navigate to Register page
    When I enter details into mandatory fields
      |first_name   |last_name   |telephone          |
      |Tester       |Testerz     |9123456789         |
    And I enter password in both password fields
      |password           |
      |TesterPassword     |
    And I click on Continue button
    Then Privacy Policy warning should be shown

