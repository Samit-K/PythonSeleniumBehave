Feature: Test Case for Verifying the Login functionality of the SauceDemo website

  @valid
  Scenario: Login to the SauceDemo website as standard user
    Given I navigated to the "Login" Page
    Then I see the title as "Swag Labs"
    And I see the "Username" field
    And I see the "Password" field
    And I see the "Login" button
    And I see the "Login Credentials"
    And I see the "Login Password"
    When I enter "Username" as "standard_user"
    And I enter "Password" as "secret_sauce"
    And I click the "Login" button
    Then I get logged in

  Scenario: Login to the SauceDemo website as locked out user
    Given I navigated to the "Login" Page
    Then I see the title as "Swag Labs"
    And I see the "Username" field
    And I see the "Password" field
    And I see the "Login" button
    And I see the "Login Credentials"
    And I see the "Login Password"
    When I enter "Username" as "locked_out_user"
    And I enter "Password" as "secret_sauce"
    And I click the "Login" button
    Then I get proper error message for "locked_out_user"

  Scenario: Login to the SauceDemo website as problem user
    Given I navigated to the "Login" Page
    Then I see the title as "Swag Labs"
    And I see the "Username" field
    And I see the "Password" field
    And I see the "Login" button
    And I see the "Login Credentials"
    And I see the "Login Password"
    When I enter "Username" as "problem_user"
    And I enter "Password" as "secret_sauce"
    And I click the "Login" button
    Then I get logged in

  Scenario: Login to the SauceDemo website as performance glitch user
    Given I navigated to the "Login" Page
    Then I see the title as "Swag Labs"
    And I see the "Username" field
    And I see the "Password" field
    And I see the "Login" button
    And I see the "Login Credentials"
    And I see the "Login Password"
    When I enter "Username" as "performance_glitch_user"
    And I enter "Password" as "secret_sauce"
    And I click the "Login" button
    Then I get logged in

  Scenario: Login to the SauceDemo website as error user
    Given I navigated to the "Login" Page
    Then I see the title as "Swag Labs"
    And I see the "Username" field
    And I see the "Password" field
    And I see the "Login" button
    And I see the "Login Credentials"
    And I see the "Login Password"
    When I enter "Username" as "error_user"
    And I enter "Password" as "secret_sauce"
    And I click the "Login" button
    Then I get logged in

  Scenario: Login to the SauceDemo website as visual user
    Given I navigated to the "Login" Page
    Then I see the title as "Swag Labs"
    And I see the "Username" field
    And I see the "Password" field
    And I see the "Login" button
    And I see the "Login Credentials"
    And I see the "Login Password"
    When I enter "Username" as "visual_user"
    And I enter "Password" as "secret_sauce"
    And I click the "Login" button
    Then I get logged in

  Scenario: Login to the SauceDemo website with empty credentials
    Given I navigated to the "Login" Page
    Then I see the title as "Swag Labs"
    And I see the "Username" field
    And I see the "Password" field
    And I see the "Login" button
    And I see the "Login Credentials"
    And I see the "Login Password"
    When I enter "Username" as ""
    And I enter "Password" as ""
    And I click the "Login" button
    Then I get proper error message for "empty credentials"

  Scenario: Login to the SauceDemo website with wrong credentials
    Given I navigated to the "Login" Page
    Then I see the title as "Swag Labs"
    And I see the "Username" field
    And I see the "Password" field
    And I see the "Login" button
    And I see the "Login Credentials"
    And I see the "Login Password"
    When I enter "Username" as "standard_user"
    And I enter "Password" as "not_secret"
    And I click the "Login" button
    Then I get proper error message for "wrong credentials"

  Scenario: Login to the SauceDemo website with no username
    Given I navigated to the "Login" Page
    Then I see the title as "Swag Labs"
    And I see the "Username" field
    And I see the "Password" field
    And I see the "Login" button
    And I see the "Login Credentials"
    And I see the "Login Password"
    When I enter "Username" as ""
    And I enter "Password" as "not_secret"
    And I click the "Login" button
    Then I get proper error message for "no username"

  Scenario: Login to the SauceDemo website with no password
    Given I navigated to the "Login" Page
    Then I see the title as "Swag Labs"
    And I see the "Username" field
    And I see the "Password" field
    And I see the "Login" button
    And I see the "Login Credentials"
    And I see the "Login Password"
    When I enter "Username" as "standard_user"
    And I enter "Password" as ""
    And I click the "Login" button
    Then I get proper error message for "no password"