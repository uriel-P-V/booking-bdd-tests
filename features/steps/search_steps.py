from behave import when, then
import requests

API_BASE_URL = "https://restful-booker.herokuapp.com"


@when("I request the current available bookings")
def step_when_list_bookings(context):

    context.response = requests.get(
        f"{API_BASE_URL}/booking"
    )


@when("I request the booking with ID {booking_id:d}")
def step_when_get_booking_by_invalid_id(context, booking_id):

    context.response = requests.get(
        f"{API_BASE_URL}/booking/{booking_id}"
    )


@when("I request the booking with the created ID")
def step_when_get_created_booking(context):

    context.response = requests.get(
        f"{API_BASE_URL}/booking/{context.booking_id}"
    )


@then("the response should contain a list of reservations")
def step_then_list_of_reservations(context):

    data = context.response.json()

    assert isinstance(data, list), "Response is not a list"

    assert len(data) > 0, "No bookings found"


@then("the response should contain reservation information")
def step_then_reservation_info(context):

    data = context.response.json()

    assert "firstname" in data

    assert "lastname" in data   