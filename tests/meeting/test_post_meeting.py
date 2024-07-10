import pytest
from core.assertions.status import *
from core.assertions.schemas import assert_payload_presentation_schema
from resources.auth.auth import Auth
from api.endpoints.meeting import MeetingEndpoints
from api.request.api_request import EspoCRMRequest
import allure

@allure.feature('Presentations - Jeyson Valdivia')
@allure.story('Create Presentations')
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
@allure.story('Create Presentations')
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
@allure.story('Create Presentations')
@pytest.mark.functional
@pytest.mark.smoke
def test_post_meeting_with_invalid_auth(get_headers, base_payload):
    url = MeetingEndpoints.create_meeting()
    headers = Auth().auth_invalid_credentials(get_headers)
    response = EspoCRMRequest.post_json(url, headers, base_payload)

    assert_status_code_unauthorized(response)

@allure.feature('Presentations - Jeyson Valdivia')
@allure.story('Create Presentations')
@pytest.mark.functional
@pytest.mark.smoke
def test_post_meetings_unauthorized(base_payload):
    url = MeetingEndpoints.create_meeting()
    response = EspoCRMRequest.post_without_headers(url, base_payload)

    assert_status_code_unauthorized(response)

@allure.feature('Presentations - Jeyson Valdivia')
@allure.story('Create Presentations')
@pytest.mark.functional
def test_post_meeting_missing_status(get_headers, base_payload):
    url = MeetingEndpoints.create_meeting()
    headers = Auth().auth_valid_credential(get_headers)
    base_payload.pop('status', None)
    response = EspoCRMRequest.post_json(url, headers, base_payload)

    assert_status_bad_request(response)

@allure.feature('Presentations - Jeyson Valdivia')
@allure.story('Create Presentations')
@pytest.mark.functional
def test_post_meeting_missing_date_start(get_headers, base_payload):
    url = MeetingEndpoints.create_meeting()
    headers = Auth().auth_valid_credential(get_headers)
    base_payload.pop('dateStart', None)
    response = EspoCRMRequest.post_json(url, headers, base_payload)

    assert_status_bad_request(response)

@allure.feature('Presentations - Jeyson Valdivia')
@allure.story('Create Presentations')
@pytest.mark.functional
def test_post_meeting_negative_duration(get_headers, base_payload):
    url = MeetingEndpoints.create_meeting()
    headers = Auth().auth_valid_credential(get_headers)
    base_payload['duration'] = -1
    response = EspoCRMRequest.post_json(url, headers, base_payload)

    assert_status_bad_request(response)

@allure.feature('Presentations - Jeyson Valdivia')
@allure.story('Create Presentations')
@pytest.mark.functional
def test_post_meeting_missing_assigned_user_id(get_headers, base_payload):
    url = MeetingEndpoints.create_meeting()
    headers = Auth().auth_valid_credential(get_headers)
    base_payload.pop('assignedUserId', None)
    response = EspoCRMRequest.post_json(url, headers, base_payload)

    assert_status_bad_request(response)

@allure.feature('Presentations - Jeyson Valdivia')
@allure.story('Create Presentations')
@pytest.mark.functional
def test_post_meeting_invalid_status(get_headers, base_payload):
    url = MeetingEndpoints.create_meeting()
    headers = Auth().auth_valid_credential(get_headers)
    base_payload['status'] = 'InvalidStatus'
    response = EspoCRMRequest.post_json(url, headers, base_payload)

    assert_status_bad_request(response)

@allure.feature('Presentations - Jeyson Valdivia')
@allure.story('Create Presentations')
@pytest.mark.functional
def test_post_meeting_without_date_end(get_headers, base_payload):
    url = MeetingEndpoints.create_meeting()
    headers = Auth().auth_valid_credential(get_headers)
    base_payload.pop('dateEnd', None)
    response = EspoCRMRequest.post_json(url, headers, base_payload)

    assert_status_bad_request(response)

@allure.feature('Presentations - Jeyson Valdivia')
@allure.story('Create Presentations')
@pytest.mark.functional
def test_post_meeting_with_all_day(get_headers, base_payload, teardown_delete_meeting):
    url = MeetingEndpoints.create_meeting()
    headers = Auth().auth_valid_credential(get_headers)
    base_payload['isAllDay'] = True
    response = EspoCRMRequest.post_json(url, headers, base_payload)

    assert_status_code_created(response)
    meeting_id = response.json().get('id')
    teardown_delete_meeting.append(meeting_id)

@allure.feature('Presentations - Jeyson Valdivia')
@allure.story('Create Presentations')
@pytest.mark.functional
def test_post_meeting_invalid_parent_type(get_headers, base_payload):
    url = MeetingEndpoints.create_meeting()
    headers = Auth().auth_valid_credential(get_headers)
    base_payload['parentType'] = 'InvalidParentType'
    response = EspoCRMRequest.post_json(url, headers, base_payload)

    assert_status_bad_request(response)

@allure.feature('Presentations - Jeyson Valdivia')
@allure.story('Create Presentations')
@pytest.mark.functional
def test_post_meeting_empty_reminder(get_headers, base_payload, teardown_delete_meeting):
    url = MeetingEndpoints.create_meeting()
    headers = Auth().auth_valid_credential(get_headers)
    base_payload['reminders'] = {}
    response = EspoCRMRequest.post_json(url, headers, base_payload)

    assert_status_code_created(response)
    meeting_id = response.json().get('id')
    teardown_delete_meeting.append(meeting_id)

@allure.feature('Presentations - Jeyson Valdivia')
@allure.story('Create Presentations')
@pytest.mark.functional
def test_post_meeting_empty_description(get_headers, base_payload, teardown_delete_meeting):
    url = MeetingEndpoints.create_meeting()
    headers = Auth().auth_valid_credential(get_headers)
    base_payload['description'] = ""
    response = EspoCRMRequest.post_json(url, headers, base_payload)

    assert_status_code_created(response)
    meeting_id = response.json().get('id')
    teardown_delete_meeting.append(meeting_id)

@allure.feature('Presentations - Jeyson Valdivia')
@allure.story('Create Presentations')
@pytest.mark.functional
def test_post_meeting_invalid_date_start_format(get_headers, base_payload):
    url = MeetingEndpoints.create_meeting()
    headers = Auth().auth_valid_credential(get_headers)
    base_payload['dateStart'] = 'InvalidDateFormat'
    response = EspoCRMRequest.post_json(url, headers, base_payload)

    assert_status_bad_request(response)

@allure.feature('Presentations - Jeyson Valdivia')
@allure.story('Create Presentations')
@pytest.mark.functional
def test_post_meeting_past_date_start(get_headers, base_payload):
    url = MeetingEndpoints.create_meeting()
    headers = Auth().auth_valid_credential(get_headers)
    base_payload['dateStart'] = '2000-01-01T00:00:00Z'
    response = EspoCRMRequest.post_json(url, headers, base_payload)

    assert_status_bad_request(response)

@allure.feature('Presentations - Jeyson Valdivia')
@allure.story('Create Presentations')
@pytest.mark.functional
def test_post_meeting_string_duration(get_headers, base_payload):
    url = MeetingEndpoints.create_meeting()
    headers = Auth().auth_valid_credential(get_headers)
    base_payload['duration'] = 'string'
    response = EspoCRMRequest.post_json(url, headers, base_payload)

    assert_status_bad_request(response)

@allure.feature('Presentations - Jeyson Valdivia')
@allure.story('Create Presentations')
@pytest.mark.functional
def test_post_meeting_string_users_ids(get_headers, base_payload):
    url = MeetingEndpoints.create_meeting()
    headers = Auth().auth_valid_credential(get_headers)
    base_payload['usersIds'] = 'string'
    response = EspoCRMRequest.post_json(url, headers, base_payload)

    assert_status_bad_request(response)

@allure.feature('Presentations - Jeyson Valdivia')
@allure.story('Create Presentations')
@pytest.mark.functional
def test_post_meeting_invalid_input_data(get_headers, base_payload):
    url = MeetingEndpoints.create_meeting()
    headers = Auth().auth_valid_credential(get_headers)
    base_payload['invalidField'] = 'InvalidData'
    response = EspoCRMRequest.post_json(url, headers, base_payload)

    assert_status_bad_request(response)

@allure.feature('Presentations - Jeyson Valdivia')
@allure.story('Create Presentations')
@pytest.mark.functional
@pytest.mark.smoke
def test_post_meeting_without_credentials(base_payload):
    url = MeetingEndpoints.create_meeting()
    response = EspoCRMRequest.post_without_headers(url, base_payload)

    assert_status_code_unauthorized(response)
