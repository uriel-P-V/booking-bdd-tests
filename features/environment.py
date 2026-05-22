from unittest.mock import patch, MagicMock

API_BASE_URL = "https://restful-booker.herokuapp.com"

# Mock data
MOCK_BOOKING_LIST = [
    {"bookingid": 1},
    {"bookingid": 2},
    {"bookingid": 3}
]

MOCK_BOOKING_DETAIL = {
    "firstname": "Uriel",
    "lastname": "Perez",
    "totalprice": 150,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2026-06-01",
        "checkout": "2026-06-05"
    }
}

MOCK_CREATED_BOOKING = {
    "bookingid": 999,
    "booking": MOCK_BOOKING_DETAIL
}

MOCK_AUTH_RESPONSE = {
    "token": "mock_token_abc123"
}

def mock_get(url, **kwargs):
    mock = MagicMock()
    if url == f"{API_BASE_URL}/ping":
        mock.status_code = 201
        mock.json.return_value = {}
    elif url == f"{API_BASE_URL}/booking":
        mock.status_code = 200
        mock.json.return_value = MOCK_BOOKING_LIST
    
    elif url == f"{API_BASE_URL}/booking/999999":
        mock.status_code = 404
        mock.text = "Not Found"

    else:
        # GET /booking/{id}
        mock.status_code = 200
        mock.json.return_value = MOCK_BOOKING_DETAIL
    return mock

def mock_post(url, **kwargs):
    mock = MagicMock()
    if url == f"{API_BASE_URL}/auth":
        mock.status_code = 200
        mock.json.return_value = MOCK_AUTH_RESPONSE
    else:
        # POST /booking
        mock.status_code = 200
        mock.json.return_value = MOCK_CREATED_BOOKING
    return mock

def mock_delete(url, **kwargs):
    mock = MagicMock()
    mock.status_code = 201
    mock.text = "Created"
    return mock


def before_scenario(context, scenario):
    print(f"Starting scenario: {scenario.name}")
    if "regression" in scenario.tags:
        context.mock_get = patch("requests.get", side_effect=mock_get)
        context.mock_post = patch("requests.post", side_effect=mock_post)
        context.mock_delete = patch("requests.delete", side_effect=mock_delete)
        
        context.mock_get.start()
        context.mock_post.start()
        context.mock_delete.start()
        

def after_scenario(context, scenario):
    print(f"Finished scenario: {scenario.name} - Status: {scenario.status}")
    if "regression" in scenario.tags:
        context.mock_get.stop()
        context.mock_post.stop()
        context.mock_delete.stop()