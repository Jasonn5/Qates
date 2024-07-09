import pytest
import json
from api_endpoints.meeting_endpoints import MeetingEndpoints
from api_endpoints.api_request import EspoCRMRequest
from resources.auth.auth import Auth
@pytest.fixture(scope="module")
def base_payload():
    with open('payloads/meeting/payload_meeting.json', 'r') as file:
        return json.load(file)


@pytest.fixture(scope="function")
def teardown_delete_meeting(get_headers):
    created_ids = []
    print("test initialized")
    yield created_ids
    for meeting_id in created_ids:
        delete_url = MeetingEndpoints.delete_meeting(meeting_id)
        headers = Auth().auth_valid_credential(get_headers)
        EspoCRMRequest.delete(delete_url, headers)