Feature: Footer validation
  Scenario: Verify footer text contains Sauce Labs
    Given I am on the login page
    Then I should see "Sauce Labs" in the footer
