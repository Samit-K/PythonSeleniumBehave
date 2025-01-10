Scenario: Open MyCart
    Given I navigated to the "Home" Page
    And I see the "Cart" Icon
    When I click the "Cart" Icon
    Then I navigated to the "Your Cart" Page
    And I see the "first two" products added to the the cart
    And I see the "Checkout" button
    When I click the the "Checkout" button
    Then I navigated to the "Checkout: Your Information" Page
    And I see the "First Name" field
    And I see the "Last Name" field
    And I see the "Postal Code" field
    And I see the "Continue" button
    When I click the the "Continue" button
    Then I navigated to the "Checkout: Overview" Page
    And I see the "Order Summary"
    And I see the "Item Total"
    And The "Item Total" on the "Checkout: Overview" page matchs the total calculated on the "Your Cart" page
