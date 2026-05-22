from behave import given, then
import requests

API_BASE_URL = "https://restful-booker.herokuapp.com"

VALID_GUEST_DATA = {
    "firstname": "Uriel",
    "lastname": "Perez",
    "totalprice": 150,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2026-06-01",
        "checkout": "2026-06-05"
    }
}


@given("the booking API is available")
def step_given_api_available(context):

    response = requests.get(f"{API_BASE_URL}/ping")

    assert response.status_code == 201, "API is not available"


@given("a reservation has been created")
def step_given_reservation_created(context):

    context.response = requests.post(
        f"{API_BASE_URL}/booking",
        json=VALID_GUEST_DATA
    )

    data = context.response.json()

    assert "bookingid" in data

    context.booking_id = data["bookingid"]


@then("the response status code should be {expected_status:d}")
def step_then_status_code(context, expected_status):

    assert (
        context.response.status_code == expected_status
    ), (
        f"Expected status code {expected_status}, "
        f"but got {context.response.status_code}"
    )