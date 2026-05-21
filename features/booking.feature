Feature: Booking API

    Background:
        Given the booking API is available

    Scenario: Create a reservation with valid data
        When I create a reservation with valid guest data
        Then the response status code should be 200
        And the response should contain the created reservation information

    Scenario: Validate that the response contains the correct fields
        When I create a reservation with valid guest data
        Then the response status code should be 200
        And the response should contain the fields:
            | firstname |
            | lastname  |
            | totalprice |
            | depositpaid |
            | bookingdates |
