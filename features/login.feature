Feature: Login Functionality
  @valid
  Scenario Outline: Login with valid credentials
    Given I navigated to login page
    When I entered valid email address as "<email>" and valid password as "<password>" into the fields
    And I click on Login button
    Then I should get logged in
    Examples:
      |email                        |password           |
      |Tester.testing@test.com      |TesterPassword     |
      |Tester.testing1@test.com     |TesterPassword1    |
      |Tester.testing2@test.com     |TesterPassword3    |

  @invalid-email
  Scenario: Login with invalid email and valid password
    Given I navigated to login page
    When I entered invalid email address and valid password as "TesterPassword" into the fields
    And I click on Login button
    Then I should get proper warning message

  @invalid-password
  Scenario: Login with valid email and invalid password
    Given I navigated to login page
    When I entered valid email address as "Tester.testing@test.com" and invalid password as "NotTesterPassword" into the fields
    And I click on Login button
    Then I should get proper warning message

  @invalid
  Scenario: Login with invalid credentials
    Given I navigated to login page
    When I entered invalid email address and invalid password as "NotTesterPassword" into the fields
    And I click on Login button
    Then I should get proper warning message

  @nocreate
  Scenario: Login without entering any credentials
    Given I navigated to login page
    When I do not enter anything into the email and password fields
    And I click on Login button
    Then I should get proper warning message