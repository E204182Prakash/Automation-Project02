Feature: Sidebar navigation
  As a SauceDemo user
  I want to use the sidebar menu
  So that I can navigate to About page or log out

  Background:
    Given I am logged in with valid credentials

  Scenario: Navigate to About page from sidebar
    When the user open the sidebar
    And the user click on About
    Then the user should be redirected to the Sauce Labs About page

  Scenario: Logout using the sidebar
    When the user open the sidebar
    And the user click on Logout
    Then the user should be redirected back to the login page
