from behave import given, when
import requests

API_BASE_URL = "https://restful-booker.herokuapp.com"


@given("a valid auth token is obtained")
def step_given_auth_token(context):

    response = requests.post(
        f"{API_BASE_URL}/auth",
        json={
            "username": "admin",
            "password": "password123"
        }
    )

    context.token = response.json()["token"]


@when("I cancel the existing reservation")
def step_when_cancel_booking(context):

    headers = {
        "Cookie": f"token={context.token}"
    }

    context.response = requests.delete(
        f"{API_BASE_URL}/booking/{context.booking_id}",
        headers=headers
    )