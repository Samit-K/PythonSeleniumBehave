Feature: Test Case for Verifying the Login and Cart functionality on SauceDemo website

  Scenario: Login to the SauceDemo website and verify the cart functionality
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

    Given I navigated to the "Products" Page
    Then I see the "Inventory List"
    And I see the "Inventory Items"
    And I see the "Cart" icon
    And I see the "Add to cart" button
    When I click the "Add to cart" button for the first two products
    Then I see the Cart icon display the number "2"

    Given I navigated to the "Products" Page
    Then I see the "Cart" icon
    When I click the "Cart" icon
    Then I navigated to the "Your Cart" Page
    And I see the "first two" products added to the cart
    And I see the "Checkout" button
    When I click the "Checkout" button
    Then I navigated to the "Checkout: Your Information" Page
    And I see the "First Name" field
    And I see the "Last Name" field
    And I see the "Zip/Postal Code" field
    And I see the "Continue" button
    When I enter "First Name" as "test_first_name"
    And I enter "Last Name" as "test_last_name"
    And I enter "Zip/Postal Code" as "123123"
    And I click the "Continue" button
    Then I navigated to the "Checkout: Overview" Page
    And I see the "Order Summary"
    And I see the "Item Total"
    And The "Item Total" on the "Checkout: Overview" page matches the total calculated on the "Your Cart" page

