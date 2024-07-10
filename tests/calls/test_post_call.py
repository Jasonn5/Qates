import allure
import pytest

from core.assertions.response_data import assert_post_response_message_bad_request
from resources.auth.auth import Auth
from api.request.api_request import EspoCRMRequest
from api.endpoints.calls import EndpointCalls
from core.assertions.payloads import assert_payload_calls
from core.assertions.schemas import assert_schema_post_call_response
from core.assertions.status import assert_status_code_created, assert_status_code_unauthorized, \
    assert_status_bad_request
from tests.conftest import encoded


@allure.suite('EspoCRM')
@allure.sub_suite('Alison')
@allure.epic('EspoCRM')
@allure.feature('Calls')
@allure.story('Post Call')
@allure.tag('author: Alison')
@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_post_create_call_with_only_required_data(get_header_cookie, base_payload_required_data_post, teardown_delete_call):
    url = EndpointCalls.post_call()
    headers = Auth().auth_valid_credential(get_header_cookie)
    response = EspoCRMRequest.post(url, headers, base_payload_required_data_post)
    assert_status_code_created(response)
    data_response = response.json()
    id_of_new_call = data_response["id"]
    teardown_delete_call.append(id_of_new_call)

    print("\n This is the ID of the call created: " + str(id_of_new_call))
    print("\n This is the status-code of the response when a call is created only with the required data: "+str(response.status_code))

@allure.suite('EspoCRM')
@allure.sub_suite('Alison')
@allure.epic('EspoCRM')
@allure.feature('Calls')
@allure.story('Post Call')
@allure.tag('author: Alison')
@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_body_request_payload(base_payload_required_data_post):
    assert_payload_calls(base_payload_required_data_post)


@allure.suite('EspoCRM')
@allure.sub_suite('Alison')
@allure.epic('EspoCRM')
@allure.feature('Calls')
@allure.story('Post Call')
@allure.tag('author: Alison')
@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_response_schema_post_call_only_required_data(get_header_cookie, base_payload_required_data_post, teardown_delete_call):
    url = EndpointCalls.post_call()
    headers = Auth().auth_valid_credential(get_header_cookie)
    response = EspoCRMRequest.post(url, headers, base_payload_required_data_post)
    assert_schema_post_call_response(response.json())
    data_response = response.json()
    id_of_new_call = data_response["id"]
    teardown_delete_call.append(id_of_new_call)


@allure.suite('EspoCRM')
@allure.sub_suite('Alison')
@allure.epic('EspoCRM')
@allure.feature('Calls')
@allure.story('Post Call')
@allure.tag('author: Alison')
@pytest.mark.functional
@pytest.mark.regression
def test_post_create_call_with_required_and_optional_data(get_header_cookie, base_payload_required_and_optional_data_post, teardown_delete_call):
    url = EndpointCalls.post_call()
    headers = Auth().auth_valid_credential(get_header_cookie)
    response = EspoCRMRequest.post(url, headers, base_payload_required_and_optional_data_post)
    assert_status_code_created(response)
    print("This is the status-code of the response when a call is created with the required and optional data: " + str(
        response.status_code))

    data_response = response.json()
    id_of_new_call = data_response["id"]
    teardown_delete_call.append(id_of_new_call)

@allure.suite('EspoCRM')
@allure.sub_suite('Alison')
@allure.epic('EspoCRM')
@allure.feature('Calls')
@allure.story('Post Call')
@allure.tag('author: Alison')
@pytest.mark.functional
@pytest.mark.regression
def test_request_payload_post_call_required_and_optional_data(base_payload_required_and_optional_data_post):
    assert_payload_calls(base_payload_required_and_optional_data_post)

@allure.suite('EspoCRM')
@allure.sub_suite('Alison')
@allure.epic('EspoCRM')
@allure.feature('Calls')
@allure.story('Post Call')
@allure.tag('author: Alison')
@pytest.mark.functional
@pytest.mark.regression
def test_response_schema_post_call_required_and_optional_data(get_header_cookie, base_payload_required_and_optional_data_post, teardown_delete_call):
    url = EndpointCalls.post_call()
    headers = Auth().auth_valid_credential(get_header_cookie)
    response = EspoCRMRequest.post(url, headers, base_payload_required_and_optional_data_post)
    assert_schema_post_call_response(response.json())
    data_response = response.json()
    id_of_new_call = data_response["id"]
    teardown_delete_call.append(id_of_new_call)

@allure.suite('EspoCRM')
@allure.sub_suite('Alison')
@allure.epic('EspoCRM')
@allure.feature('Calls')
@allure.story('Post Call')
@allure.tag('author: Alison')
@pytest.mark.functional
@pytest.mark.regression
def test_post_call_invalid_cookie_in_headers(get_header_cookie, base_payload_required_data_post, teardown_delete_call):
    url = EndpointCalls.post_call()
    headers = Auth().auth_valid_credential(get_header_cookie)
    headers['Cookie'] = 'wrongCookie'
    response = EspoCRMRequest.post(url, headers, base_payload_required_data_post)
    assert_status_code_unauthorized(response)

    data_response = response.json()
    id_of_new_call = data_response["id"]
    teardown_delete_call.append(id_of_new_call)

@allure.suite('EspoCRM')
@allure.sub_suite('Alison')
@allure.epic('EspoCRM')
@allure.feature('Calls')
@allure.story('Post Call')
@allure.tag('author: Alison')
@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_post_call_invalid_authorization_in_headers(get_header_cookie, base_payload_required_data_post, teardown_delete_call):
    url = EndpointCalls.post_call()
    headers = Auth().auth_valid_credential(get_header_cookie)
    invalidAuth = encoded("invalidUser1232","invalidPassword456")
    headers['Authorization'] = 'Basic '+invalidAuth
    response = EspoCRMRequest.post(url, headers, base_payload_required_data_post)
    assert_status_code_unauthorized(response)

@allure.suite('EspoCRM')
@allure.sub_suite('Alison')
@allure.epic('EspoCRM')
@allure.feature('Calls')
@allure.story('Post Call')
@allure.tag('author: Alison')
@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_post_call_invalid_data_in_dateStart_required_field_in_payload(get_header_cookie, base_payload_required_data_post, teardown_delete_call):
    url = EndpointCalls.post_call()
    headers = Auth().auth_valid_credential(get_header_cookie)
    payload_invalid_required_data = base_payload_required_data_post
    payload_invalid_required_data['dateStart'] = '-//*-3430?=?)='
    response = EspoCRMRequest.post(url, headers, base_payload_required_data_post)
    assert_status_bad_request(response)
    print(response.json())
    assert_post_response_message_bad_request(response.json())

@allure.suite('EspoCRM')
@allure.sub_suite('Alison')
@allure.epic('EspoCRM')
@allure.feature('Calls')
@allure.story('Post Call')
@allure.tag('author: Alison')
@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_post_call_invalid_data_in_direction_required_field_in_payload(get_header_cookie, base_payload_required_data_post, teardown_delete_call):
    url = EndpointCalls.post_call()
    headers = Auth().auth_valid_credential(get_header_cookie)
    payload_invalid_required_data = base_payload_required_data_post
    payload_invalid_required_data['direction'] = '-//*-3430?=?)='
    response = EspoCRMRequest.post(url, headers, base_payload_required_data_post)
    assert_status_bad_request(response)
    print(response.json())
    assert_post_response_message_bad_request(response.json())

