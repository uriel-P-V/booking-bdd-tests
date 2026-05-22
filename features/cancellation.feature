Feature: Cancellation API

  Background:
    Given the booking API is available
    And a valid auth token is obtained
    And a reservation has been created

  Scenario: Cancel an existing reservation
    When I cancel the existing reservation
    Then the response status code should be 201