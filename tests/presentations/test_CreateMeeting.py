import requests
import json
from config import BASE_URI
from src.assertions.assertion_status import assert_status_code_created
from src.assertions.assertion_headers import assert_content_type_applicationJson
from src.assertions.assertion_comparison import assert_equal_to
from src.resources.auth.auth import Auth
from src.espocrm_api.meetring_endpoints import EndpointMeetings


with open('src/payloads/meeting_payload.json', 'r') as file:
    BASE_PAYLOAD = json.load(file)

def create_meeting_with_payload(get_headers, payload_modification):
    url = f"{BASE_URI}{EndpointMeetings.CREATE_MEETING.value}"
    payload = BASE_PAYLOAD.copy()
    payload.update(payload_modification)
    headers = Auth().auth_valid_credential(get_headers)
    return requests.post(url, headers=headers, json=payload)

def test_create_meeting_all_valid(get_headers):
    response = create_meeting_with_payload(get_headers, {})
    assert_status_code_created(response)
    assert_content_type_applicationJson(response)
    response_data = response.json()
    assert_equal_to(response_data["status"], "Planned")

def test_create_meeting_no_date_end(get_headers):
    response = create_meeting_with_payload(get_headers, {"dateEnd": None})
    assert_status_code_created(response)
    response_data = response.json()
    assert_equal_to(response_data["status"], "Planned")
