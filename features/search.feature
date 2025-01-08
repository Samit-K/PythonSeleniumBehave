Feature: Search Functionality

  @valid
  Scenario: Search for a valid product
    Given I got navigated to home page
    When I enter valid product name "HP" into the Search box
    And I click on Search button
    Then Valid product should get displayed in Search results

  @invalid
  Scenario: Search for an invalid product
    Given I got navigated to home page
    When I enter invalid product name "Honda" into the Search box
    And I click on Search button
    Then Proper message should be displayed in Search results

  @no_product
  Scenario: Search without entering any product
    Given I got navigated to home page
    When I dont enter anything into the Search box
    And I click on Search button
    Then Proper message should be displayed in Search results