import pytest
from assertions.assertion_status import *
from assertions.assertion_schemas import assert_payload_presentation_schema
from resources.auth.auth import Auth
from api_endpoints.meeting_endpoints import MeetingEndpoints
from api_endpoints.api_request import EspoCRMRequest
import allure

@allure.feature('Presentations - Jeyson Valdivia')
@allure.story('Get Presentations')
@pytest.mark.functional
@pytest.mark.smoke
def test_post_meeting_success(get_headers, base_payload, teardown_delete_meeting):
    url = MeetingEndpoints.create_meeting()
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.post_json(url, headers, base_payload)

    assert_status_code_created(response)
    meeting_id = response.json().get('id')
    teardown_delete_meeting.append(meeting_id)

@allure.feature('Presentations - Jeyson Valdivia')
@allure.story('Get Presentations')
@pytest.mark.functional
@pytest.mark.regression
def test_post_meetings_schema_validation(get_headers, base_payload, teardown_delete_meeting):
    url = MeetingEndpoints.create_meeting()
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.post_json(url, headers, base_payload)

    assert_payload_presentation_schema(response.json())
    meeting_id = response.json().get('id')
    teardown_delete_meeting.append(meeting_id)
@allure.feature('Presentations - Jeyson Valdivia')
@allure.story('Get Presentations')
@pytest.mark.functional
@pytest.mark.smoke
def test_post_meeting_with_invalid_auth(get_headers, base_payload):
    url = MeetingEndpoints.create_meeting()
    headers = Auth().auth_invalid_credentials(get_headers)
    response = EspoCRMRequest.post_json(url, headers, base_payload)

    assert_status_code_unauthorized(response)

@allure.feature('Presentations - Jeyson Valdivia')
@allure.story('Get Presentations')
@pytest.mark.functional
@pytest.mark.smoke
def test_post_meetings_unauthorized(base_payload):
    url = MeetingEndpoints.create_meeting()
    response = EspoCRMRequest.post_without_headers(url,base_payload)

    assert_status_code_unauthorized(response)