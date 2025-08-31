Feature: Checkout process
  As a SauceDemo user
  I want to purchase a product
  So that I can complete an order successfully

  Background:
    Given I am logged in with valid credentials
    And I have added a product to the cart

  Scenario: Complete checkout successfully
    When the user proceed to checkout
    And the user provide checkout information
    And the user finish the order
    Then the user should see the success message
