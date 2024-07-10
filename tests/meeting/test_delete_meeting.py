import pytest
from core.assertions.status import *
from resources.auth.auth import Auth
from api.endpoints.meeting import MeetingEndpoints
from api.request.api_request import EspoCRMRequest
from core.assertions.headers import *
from core.assertions.comparison import assert_equal_to
import allure

@allure.suite('EspoCRM')
@allure.sub_suite('Jeyson')
@allure.epic('EspoCRM')
@allure.feature('Meetings')
@allure.story('Delete Meeting')
@allure.tag('author: Jeyson')
@pytest.mark.functional
@pytest.mark.smoke
def test_delete_existing_meeting(setup_create_meeting):
    headers, meeting_id = setup_create_meeting
    delete_url = MeetingEndpoints.delete_meeting(meeting_id)
    response = EspoCRMRequest.delete(delete_url, headers)
    assert_status_code_ok(response)

@allure.suite('EspoCRM')
@allure.sub_suite('Jeyson')
@allure.epic('EspoCRM')
@allure.feature('Meetings')
@allure.story('Delete Meeting')
@allure.tag('author: Jeyson')
@allure.feature('Presentations - Jeyson Valdivia')
@allure.story('Delete Presentations')
@pytest.mark.functional
@pytest.mark.regression
def test_delete_non_existent_meeting(get_headers):
    non_existent_meeting_id = "nonExistentMeetingId"
    url = MeetingEndpoints.delete_meeting(non_existent_meeting_id)
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.delete(url, headers)
    assert_status_code_not_found(response)

@allure.suite('EspoCRM')
@allure.sub_suite('Jeyson')
@allure.epic('EspoCRM')
@allure.feature('Meetings')
@allure.story('Delete Meeting')
@allure.tag('author: Jeyson')
@allure.feature('Presentations - Jeyson Valdivia')
@allure.story('Delete Presentations')
@pytest.mark.smoke
@pytest.mark.functional
def test_delete_meeting_without_auth(setup_create_meeting):
    _, meeting_id = setup_create_meeting
    delete_url = MeetingEndpoints.delete_meeting(meeting_id)
    response = EspoCRMRequest.delete_without_headers(delete_url)
    assert_status_code_unauthorized(response)

@allure.suite('EspoCRM')
@allure.sub_suite('Jeyson')
@allure.epic('EspoCRM')
@allure.feature('Meetings')
@allure.story('Delete Meeting')
@allure.tag('author: Jeyson')
@allure.feature('Presentations - Jeyson Valdivia')
@allure.story('Delete Presentations')
@pytest.mark.functional
@pytest.mark.smoke
def test_delete_meeting_returns_ok(setup_create_meeting):
    headers, meeting_id = setup_create_meeting
    delete_url = MeetingEndpoints.delete_meeting(meeting_id)
    response = EspoCRMRequest.delete(delete_url, headers)
    assert_status_code_ok(response)

@allure.suite('EspoCRM')
@allure.sub_suite('Jeyson')
@allure.epic('EspoCRM')
@allure.feature('Meetings')
@allure.story('Delete Meeting')
@allure.tag('author: Jeyson')
@allure.feature('Presentations - Jeyson Valdivia')
@allure.story('Delete Presentations')
@pytest.mark.functional
@pytest.mark.regression
def test_deleted_meeting_not_recoverable(get_headers, setup_create_meeting):
    headers, meeting_id = setup_create_meeting
    delete_url = MeetingEndpoints.delete_meeting(meeting_id)
    delete_response = EspoCRMRequest.delete(delete_url, headers)
    assert_status_code_ok(delete_response)
    get_url = MeetingEndpoints.get_meeting_by_id(meeting_id)
    get_response = EspoCRMRequest.get_with_url_headers(get_url, headers)
    assert_status_code_not_found(get_response)

@allure.suite('EspoCRM')
@allure.sub_suite('Jeyson')
@allure.epic('EspoCRM')
@allure.feature('Meetings')
@allure.story('Delete Meeting')
@allure.tag('author: Jeyson')
@allure.feature('Presentations - Jeyson Valdivia')
@allure.story('Delete Presentations')
@pytest.mark.functional
@pytest.mark.regression
def test_delete_meeting_invalid_id(get_headers):
    invalid_meeting_id = "invalidId!@#"
    url = MeetingEndpoints.delete_meeting(invalid_meeting_id)
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.delete(url, headers)
    assert_status_code_not_found(response)

@allure.suite('EspoCRM')
@allure.sub_suite('Jeyson')
@allure.epic('EspoCRM')
@allure.feature('Meetings')
@allure.story('Delete Meeting')
@allure.tag('author: Jeyson')
@allure.feature('Presentations - Jeyson Valdivia')
@allure.story('Delete Presentations')
@pytest.mark.smoke
@pytest.mark.functional
def test_delete_meeting_unauthorized_user(get_headers, setup_create_meeting):
    _, meeting_id = setup_create_meeting
    delete_url = MeetingEndpoints.delete_meeting(meeting_id)
    unauthorized_headers = Auth().auth_invalid_credentials(get_headers)
    response = EspoCRMRequest.delete(delete_url, unauthorized_headers)
    assert_status_code_unauthorized(response)

@allure.suite('EspoCRM')
@allure.sub_suite('Jeyson')
@allure.epic('EspoCRM')
@allure.feature('Meetings')
@allure.story('Delete Meeting')
@allure.tag('author: Jeyson')
@allure.feature('Presentations - Jeyson Valdivia')
@allure.story('Delete Presentations')
@pytest.mark.functional
def test_delete_meeting_expected_headers(get_headers, setup_create_meeting):
    headers, meeting_id = setup_create_meeting
    delete_url = MeetingEndpoints.delete_meeting(meeting_id)
    delete_response = EspoCRMRequest.delete(delete_url, headers)
    assert_status_code_ok(delete_response)
    assert_content_type_application_json(delete_response)
    assert 'Date' in delete_response.headers
    assert 'Server' in delete_response.headers

@allure.suite('EspoCRM')
@allure.sub_suite('Jeyson')
@allure.epic('EspoCRM')
@allure.feature('Meetings')
@allure.story('Delete Meeting')
@allure.tag('author: Jeyson')
@allure.feature('Presentations - Jeyson Valdivia')
@allure.story('Delete Presentations')
@pytest.mark.functional
def test_delete_meeting_confirmation_response_body(get_headers, setup_create_meeting):
    headers, meeting_id = setup_create_meeting
    delete_url = MeetingEndpoints.delete_meeting(meeting_id)
    delete_response = EspoCRMRequest.delete(delete_url, headers)
    assert_status_code_ok(delete_response)
    assert_equal_to(delete_response.text, 'true')
