Feature: Search Booking API

  Background:
    Given the booking API is available
    And a reservation has been created

  @smoke
  Scenario: List all available reservations
    When I request the current available bookings
    Then the response status code should be 200
    And the response should contain a list of reservations
  
  @regression
  Scenario: Get a reservation by valid ID
    When I request the booking with the created ID
    Then the response status code should be 200
    And the response should contain reservation information
  @regression
  Scenario: Get a reservation by invalid ID
    When I request the booking with ID 999999
    Then the response status code should be 404