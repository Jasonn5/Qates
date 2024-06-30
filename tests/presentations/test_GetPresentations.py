from src.assertions.assertion_schemas import assert_schema_presentation
import requests
from config import BASE_URI, MEETING_PARAM
from src.assertions.assertion_status import *
from src.assertions.assertion_headers import assert_content_type_applicationJson
from src.assertions.assertion_comparison import *
from src.resources.auth.auth import Auth
from src.espocrm_api.meetring_endpoints import EndpointMeetings

def test_get_meetings_success(get_headers):
    url = f"{BASE_URI}{EndpointMeetings.GET_MEETINGS_WITHOUT_PARAMS.value}"
    response = requests.get(url, headers=Auth().auth_valid_credential(get_headers))
    assert_status_code_ok(response)

def test_get_meetings_schema_validation(get_headers):
    url = f"{BASE_URI}{EndpointMeetings.GET_MEETINGS_WITHOUT_PARAMS.value}"
    response = requests.get(url, headers= Auth().auth_valid_credential(get_headers))
    assert_schema_presentation(response.json())

def test_get_meetings_response_format(get_headers):
    url = f"{BASE_URI}{EndpointMeetings.GET_MEETINGS_WITHOUT_PARAMS.value}"
    response = requests.get(url, headers=Auth().auth_valid_credential(get_headers))
    assert_content_type_applicationJson(response)

def test_get_meetings_max_size(get_headers):
    url = f"{BASE_URI}{EndpointMeetings.GET_MEETINGS_WITH_PARAMS.value}"
    max_size = 1
    MEETING_PARAM['maxSize'] = max_size
    response = requests.get(url, params=MEETING_PARAM, headers=Auth().auth_valid_credential(get_headers))
    data = response.json()['list']
    assert_less_than_or_equal_to(len(data), max_size)

def test_get_meetings_unauthorized():
    url = f"{BASE_URI}{EndpointMeetings.GET_MEETINGS_WITHOUT_PARAMS.value}"
    response = requests.get(url)
    assert_status_code_unauthorized(response)

def test_get_meetings_invalid_auth(get_headers):
    url = f"{BASE_URI}{EndpointMeetings.GET_MEETINGS_WITHOUT_PARAMS.value}"
    headers = Auth().auth_invalid_credentials(get_headers)
    response = requests.get(url, headers=headers)
    assert_status_code_unauthorized(response)


def test_get_meetings_pagination(get_headers):
    headers = Auth().auth_valid_credential(get_headers)
    max_size = 2
    MEETING_PARAM['maxSize'] = max_size
    url = f"{BASE_URI}{EndpointMeetings.GET_MEETINGS_WITH_PARAMS.value}"
    response_without_offset = requests.get(url, params=MEETING_PARAM, headers=headers)
    offset = 1
    MEETING_PARAM_WITH_OFFSET = MEETING_PARAM.copy()
    MEETING_PARAM_WITH_OFFSET['offset'] = offset
    response_with_offset = requests.get(url, params=MEETING_PARAM_WITH_OFFSET, headers=headers)

    assert_status_code_ok(response_with_offset)
    assert_status_code_ok(response_without_offset)

    data_with_offset = response_with_offset.json()
    data_without_offset = response_without_offset.json()
    data_list_with_offset = data_with_offset["list"]
    data_list_without_offset = data_without_offset["list"]

    assert_less_than_or_equal_to(len(data_list_with_offset), max_size)

    if len(data_list_without_offset) > offset:
        expected_first_item_with_offset = data_list_without_offset[offset]

        actual_first_item_with_offset = data_list_with_offset[0]
        assert_equal_to(actual_first_item_with_offset["id"], expected_first_item_with_offset["id"])


def test_get_meetings_order_desc(get_headers):
    MEETING_PARAM['order'] = 'desc'
    url = f"{BASE_URI}{EndpointMeetings.GET_MEETINGS_WITH_PARAMS.value}"
    response = requests.get(url, params= MEETING_PARAM, headers=Auth().auth_valid_credential(get_headers))

    assert_status_code_ok(response)

    data = response.json()
    meetings_list = data["list"]
    dates = [item['dateStart'] for item in meetings_list]

    assert_equal_to(dates, sorted(dates, reverse=True))

def test_get_meetings_order_asc(get_headers):
    url = f"{BASE_URI}{EndpointMeetings.GET_MEETINGS_WITH_PARAMS.value}"
    MEETING_PARAM['order'] = 'asc'
    response = requests.get(url, params=MEETING_PARAM, headers=Auth().auth_valid_credential(get_headers))

    assert_status_code_ok(response)

    data = response.json()
    meetings_list = data["list"]
    dates = [item['dateStart'] for item in meetings_list]

    assert_equal_to(dates, sorted(dates))

#It's a bug the API is accepting invalid parameters, current result 200, expected result 400
def test_get_meetings_invalid_param(get_headers):
    url = f"{BASE_URI}{EndpointMeetings.GET_MEETINGS_WITH_PARAMS.value}invalidParam=value"
    response = requests.get(url, headers=Auth().auth_valid_credential(get_headers))

    assert_status_bad_request(response)