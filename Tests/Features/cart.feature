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
