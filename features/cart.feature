Feature: Add and modify items in cart

  @add_item
  Scenario: Add an item to the cart
    Given I got navigated to home page
    When I click on a product
    And I put desired quantity
    And I click on Add to Cart button
    Then I should see a message telling me I added the item(s) to cart

  @remove
  Scenario: Remove an item from the cart
    Given I got navigated to the cart page
    When I click on the remove item button
    Then I should see the item removed from the cart

  @modify
  Scenario: Modify quantity for the item in the cart
    Given I got navigated to the cart page
    When I change the quantity
    And I click on the update button
    Then I should see an updated Total Value