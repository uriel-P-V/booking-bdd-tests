from behave import when, then
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


@when("I create a reservation with valid guest data")
def step_when_create_booking(context):
    context.response = requests.post(f"{API_BASE_URL}/booking", json=VALID_GUEST_DATA)

    
@then("the response should contain the created reservation information")
def step_then_created_reservation(context):
    data = context.response.json()

    assert "bookingid" in data
    assert "booking" in data

    #también debe ser objeto JSON válido.
    assert isinstance(data["booking"],dict)
    assert isinstance(data["bookingid"], int)


    context.booking_id = data["bookingid"]


@then("the response should contain the fields:")
def step_then_contains_fields(context):
    booking_data= context.response.json()["booking"]
    for row in context.table:
        field = row[0]
        assert field in booking_data, f"{field} not found in response"
    