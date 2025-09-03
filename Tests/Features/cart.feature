Feature: Add product to cart
  As a SauceDemo user
  I want to add a product to the shopping cart
  So that I can proceed to checkout

  Background:
    Given I am logged in with valid credentials

  Scenario: Add an item to the cart successfully
    When the user add a product to the cart
    And the user navigate to the cart page
    Then the user should see the product in the cart

  Scenario: Remove an item from the cart
    When the user add a product to the cart
    And the user removes the item from the cart
    Then the cart should be empty
  
  Scenario: Proceed to checkout
    When the user add a product to the cart
    And the user navigate to the cart page
    And the user proceeds to checkout
    Then the checkout page should be displayed