import pytest
from api_endpoints.api_request import EspoCRMRequest
from config.config import MEETING_PARAM
from assertions.assertion_schemas import assert_schema_presentation
from assertions.assertion_status import assert_status_code_ok, assert_status_code_unauthorized, assert_status_bad_request
from assertions.assertion_headers import assert_content_type_application_json
from assertions.assertion_comparison import assert_less_than_or_equal_to, assert_equal_to
from resources.auth.auth import Auth
from api_endpoints.meeting_endpoints import MeetingEndpoints

@pytest.mark.smoke
@pytest.mark.functional
def test_get_meetings_success(get_headers):
    url = MeetingEndpoints.get_meeting_without_params()
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.get_with_url_headers(url, headers)
    assert_status_code_ok(response)

@pytest.mark.functional
@pytest.mark.regression
def test_get_meetings_schema_validation(get_headers):
    url = MeetingEndpoints.get_meeting_without_params()
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.get_with_url_headers(url, headers)
    assert_schema_presentation(response.json())

@pytest.mark.functional
def test_get_meetings_response_format(get_headers):
    url = MeetingEndpoints.get_meeting_without_params()
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.get_with_url_headers(url, headers)
    assert_content_type_application_json(response)

@pytest.mark.functional
def test_get_meetings_max_size(get_headers):
    params = MEETING_PARAM.copy()
    params['maxSize'] = 1
    url = MeetingEndpoints.get_meeting_with_params(params=params)
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.get_with_url_headers_params(url, params, headers)
    data = response.json()['list']
    assert_less_than_or_equal_to(len(data), 1)

@pytest.mark.smoke
@pytest.mark.functional
def test_get_meetings_unauthorized():
    url = MeetingEndpoints.get_meeting_without_params()
    response = EspoCRMRequest.get_with_url(url)
    assert_status_code_unauthorized(response)

@pytest.mark.smoke
@pytest.mark.functional
def test_get_meetings_invalid_auth(get_headers):
    url = MeetingEndpoints.get_meeting_without_params()
    headers = Auth().auth_invalid_credentials(get_headers)
    response = EspoCRMRequest.get_with_url_headers(url, headers)
    assert_status_code_unauthorized(response)

@pytest.mark.functional
def test_get_meetings_pagination(get_headers):
    headers = Auth().auth_valid_credential(get_headers)
    max_size = 2
    params = MEETING_PARAM.copy()
    params['maxSize'] = max_size
    url = MeetingEndpoints.get_meeting_with_params(params=params)
    response_without_offset = EspoCRMRequest.get_with_url_headers_params(url, params, headers)
    offset = 1
    params_with_offset = params.copy()
    params_with_offset['offset'] = offset
    response_with_offset = EspoCRMRequest.get_with_url_headers_params(url, params_with_offset, headers)

    assert_status_code_ok(response_without_offset)
    assert_status_code_ok(response_with_offset)

    data_with_offset = response_with_offset.json()
    data_without_offset = response_without_offset.json()
    data_list_with_offset = data_with_offset["list"]
    data_list_without_offset = data_without_offset["list"]

    assert_less_than_or_equal_to(len(data_list_with_offset), max_size)

    if len(data_list_without_offset) > offset:
        expected_first_item_with_offset = data_list_without_offset[offset]
        actual_first_item_with_offset = data_list_with_offset[0]
        assert_equal_to(actual_first_item_with_offset["id"], expected_first_item_with_offset["id"])

@pytest.mark.functional
@pytest.mark.regression
def test_get_meetings_order_desc(get_headers):
    params = MEETING_PARAM.copy()
    params['order'] = 'desc'
    url = MeetingEndpoints.get_meeting_with_params(params=params)
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.get_with_url_headers_params(url, params, headers)

    assert_status_code_ok(response)

    data = response.json()
    meetings_list = data["list"]
    dates = [item['dateStart'] for item in meetings_list]

    assert_equal_to(dates, sorted(dates, reverse=True))

@pytest.mark.functional
@pytest.mark.regression
def test_get_meetings_order_asc(get_headers):
    params = MEETING_PARAM.copy()
    params['order'] = 'asc'
    url = MeetingEndpoints.get_meeting_with_params(params=params)
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.get_with_url_headers_params(url, params, headers)

    assert_status_code_ok(response)

    data = response.json()
    meetings_list = data["list"]
    dates = [item['dateStart'] for item in meetings_list]

    assert_equal_to(dates, sorted(dates))

@pytest.mark.functional
def test_get_meetings_invalid_param(get_headers):
    params = MEETING_PARAM.copy()
    params['invalidParam'] = 'value'
    url = MeetingEndpoints.get_meeting_with_params(params=params)
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.get_with_url_headers_params(url, params, headers)

    assert_status_bad_request(response)
