Feature: Cancellation API

    Background:
        Given the booking API is available

    Scenario: Cancel an existing reservation
        When I cancel the booking with ID 4760
        Then the response status code should be 200