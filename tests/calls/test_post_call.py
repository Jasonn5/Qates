import pytest

from api_endpoints.api_request import EspoCRMRequest
from api_endpoints.calls_endpoints import EndpointCalls
from assertions.assertion_payloads import assert_payload_calls
from assertions.assertion_schemas import assert_schema_post_call_response
from assertions.assertion_status import assert_status_code_created, assert_status_code_unauthorized
from config.config import USERNAME, PASSWORD, CALL_REQUIRED_AND_OPTIONAL_DATA
from payloads.calls.pyload_call import call_payload_required_data
from tests.calls.conftest import teardown_call
from tests.conftest import encoded


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_post_create_call_with_only_required_data(get_header_cookie):
    url = EndpointCalls.post_call()
    payload_required_data = call_payload_required_data
    headers = get_header_cookie(USERNAME, PASSWORD)
    response = EspoCRMRequest.post(url, headers, payload_required_data)
    assert_status_code_created(response)
    data_response = response.json()
    id_of_new_call = data_response["id"]
    teardown_call(id_of_new_call, headers)

    print("\n This is the ID of the call created: " + str(id_of_new_call))
    print("\n This is the status-code of the response when a call is created only with the required data: "+str(response.status_code))

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_body_request_payload(get_header_cookie):
    url = EndpointCalls.post_call()
    data_payload = call_payload_required_data
    headers = get_header_cookie(USERNAME, PASSWORD)
    assert_payload_calls(data_payload)

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_response_schema_post_call_only_required_data(get_header_cookie):
    url = EndpointCalls.post_call()
    payload_required_data = call_payload_required_data
    headers = get_header_cookie(USERNAME, PASSWORD)
    response = EspoCRMRequest.post(url, headers, payload_required_data)
    assert_schema_post_call_response(response.json())
    data_response = response.json()
    id_of_new_call = data_response["id"]
    teardown_call(id_of_new_call, headers)

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_post_create_call_with_required_and_optional_data(get_header_cookie):
    url = EndpointCalls.post_call()
    payload_required_and_optional_data = call_payload_required_data

    headers = get_header_cookie(USERNAME, PASSWORD)
    response = EspoCRMRequest.post(url, headers, payload_required_and_optional_data)
    assert_status_code_created(response)
    print("This is the status-code of the response when a call is created with the required and optional data: " + str(
        response.status_code))

    data_response = response.json()
    id_of_new_call = data_response["id"]
    teardown_call(id_of_new_call, headers)

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_request_payload_post_call_required_and_optional_data(get_header_cookie):
    url = EndpointCalls.post_call()
    payload_required_and_optional_data = call_payload_required_data
    headers = get_header_cookie(USERNAME, PASSWORD)
    assert_payload_calls(payload_required_and_optional_data)

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_post_call_invalid_cookie_in_headers(get_header_cookie):
    url = EndpointCalls.post_call()
    headers = get_header_cookie(USERNAME, PASSWORD)
    headers['Cookie'] = 'wrongCookie'
    payload_required_data = call_payload_required_data
    response = EspoCRMRequest.post(url, headers, payload_required_data)
    assert_status_code_unauthorized(response)

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_post_call_invalid_authorization_in_headers(get_header_cookie):
    url = EndpointCalls.post_call()
    headers = get_header_cookie(USERNAME, PASSWORD)
    invalidAuth = encoded("invalidUser1232","invalidPassword456")
    headers['Authorization'] = 'Basic '+invalidAuth
    payload_required_data = call_payload_required_data
    response = EspoCRMRequest.post(url, headers, payload_required_data)
    assert_status_code_unauthorized(response)
    