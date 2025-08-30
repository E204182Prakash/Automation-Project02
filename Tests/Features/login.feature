Feature: Login functionality
  As a user of the SauceDemo site
  I want to login with valid credentials
  So that I can access my inventory page

  Background:
    Given I am on the login page

  Scenario: Successful login with valid credentials
    When the user enter valid username and password
    And the user click the login button
    Then the user should see the inventory page

  Scenario: Failed login with invalid credentials
    When the user enter invalid username and password
    And the user click the login button
    Then the user should see an error message
