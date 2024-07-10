import pytest
import json
from api.endpoints.meeting import MeetingEndpoints
from api.request.api_request import EspoCRMRequest
from resources.auth.auth import Auth

@pytest.fixture(scope="module")
def base_payload():
    with open('core/payloads/meeting/payload_meeting.json', 'r') as file:
        return json.load(file)

@pytest.fixture(scope="function")
def setup_create_meeting(get_headers, base_payload):
    headers = Auth().auth_valid_credential(get_headers)
    url = MeetingEndpoints.create_meeting()
    response = EspoCRMRequest.post_json(url, headers, base_payload)
    meeting_id = response.json().get('id')

    yield headers, meeting_id

@pytest.fixture(scope="function")
def teardown_delete_meeting(get_headers):
    created_ids = []
    print("test initialized")
    yield created_ids
    for meeting_id in created_ids:
        delete_url = MeetingEndpoints.delete_meeting(meeting_id)
        headers = Auth().auth_valid_credential(get_headers)
        EspoCRMRequest.delete(delete_url, headers)

@pytest.fixture(scope="function")
def setup_teardown_meeting(get_headers, base_payload):
    headers = Auth().auth_valid_credential(get_headers)
    url = MeetingEndpoints.create_meeting()
    response = EspoCRMRequest.post_json(url, headers, base_payload)
    meeting_id = response.json().get('id')

    yield headers, meeting_id

    delete_url = MeetingEndpoints.delete_meeting(meeting_id)
    EspoCRMRequest.delete(delete_url, headers)