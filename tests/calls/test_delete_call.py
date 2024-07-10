from copy import deepcopy

import allure
import pytest

from api.request.api_request import EspoCRMRequest
from api.endpoints.calls import EndpointCalls
from core.assertions.calls import assert_delete_success_response_message, assert_delete_failed_response_message, \
    assert_created_success_response_deleted_field, assert_deleted_success_response_deleted_field
from core.assertions.headers import assert_content_type_application_json
from core.assertions.status import assert_status_code_ok, assert_status_code_not_found, assert_status_bad_request, \
    assert_status_code_unauthorized
from tests.conftest import encoded
from resources.auth.auth import Auth


@allure.suite('EspoCRM')
@allure.sub_suite('Alison')
@allure.epic('EspoCRM')
@allure.feature('Calls')
@allure.story('Delete Call')
@allure.tag('author: Alison')
@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
#Verify that deleting a call with invalid authentication returns 401
def test_delete_call_with_invalid_authentication(setup_create_call):
    headers, id_of_new_call = setup_create_call
    invalid_authorization_header = headers
    invalidAuth = encoded("invalidUser1232", "invalidPassword456")
    invalid_authorization_header['Authorization'] = 'Basic ' + invalidAuth

    url_delete = EndpointCalls.delete_call(id_of_new_call)
    response_delete = EspoCRMRequest.delete(url_delete, invalid_authorization_header)
    assert_status_code_unauthorized(response_delete)

    response_delete = EspoCRMRequest.delete(url_delete, headers)
@allure.suite('EspoCRM')
@allure.sub_suite('Alison')
@allure.epic('EspoCRM')
@allure.feature('Calls')
@allure.story('Delete Call')
@allure.tag('author: Alison')
@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
#Verify that an existing call can be deleted - status code 200 and response message
def test_delete_call_successful(setup_create_call):
    headers, id_of_new_call = setup_create_call
    url_delete = EndpointCalls.delete_call(id_of_new_call)
    response_delete = EspoCRMRequest.delete(url_delete, headers)
    assert_status_code_ok(response_delete)
    assert_delete_success_response_message(response_delete)

@allure.suite('EspoCRM')
@allure.sub_suite('Alison')
@allure.epic('EspoCRM')
@allure.feature('Calls')
@allure.story('Delete Call')
@allure.tag('author: Alison')
@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
#Verify that a deleted call cannot be recovered afterwards
def test_delete_call_recoverable_with_deleted_field_true(setup_create_call_get_response):
    headers, id_of_new_call, call_created_response = setup_create_call_get_response
    assert_created_success_response_deleted_field(call_created_response)

    url_delete = EndpointCalls.delete_call(id_of_new_call)
    response_delete = EspoCRMRequest.delete(url_delete, headers)
    assert_status_code_ok(response_delete)
    assert_delete_success_response_message(response_delete)
    print("Response message: " + str(response_delete.text.strip()))

    url_get_by_id = f"{EndpointCalls.get_call_without_params()}/{id_of_new_call}"
    response_get_call_by_id = EspoCRMRequest.get_with_url_headers(url_get_by_id, headers)
    assert_deleted_success_response_deleted_field(response_get_call_by_id)
    assert_status_code_ok(response_get_call_by_id)

@allure.suite('EspoCRM')
@allure.sub_suite('Alison')
@allure.epic('EspoCRM')
@allure.feature('Calls')
@allure.story('Delete Call')
@allure.tag('author: Alison')
@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
# Verify deletion of more than one call- status code 200 OK
def test_delete_more_than_one_call(setup_create_call, base_payload_delete):
    headers, id_of_new_call_1 = setup_create_call
    headers, id_of_new_call_2 = setup_create_call
    headers, id_of_new_call_3 = setup_create_call

    payload_delete_calls = base_payload_delete
    delete_more_than_one_call_url = EndpointCalls.delete_call_more_than_one_call()
    payload_delete_calls["params"]["ids"] = [id_of_new_call_1, id_of_new_call_2, id_of_new_call_3]

    response_delete = EspoCRMRequest.delete_more_than_one_item(delete_more_than_one_call_url, headers, payload_delete_calls)
    assert_status_code_ok(response_delete)


''' The result of this Test Case is a BUG, because instead of using the verb DELETE to delete more than on call,
The system uses a POST, which is the wrong VERB, sending a body with the IDs of all the call to be eliminated'''

@allure.suite('EspoCRM')
@allure.sub_suite('Alison')
@allure.epic('EspoCRM')
@allure.feature('Calls')
@allure.story('Delete Call')
@allure.tag('author: Alison')
@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
# Verify that deleting a non-existent call returns 404
def test_delete_non_existing_call(get_header_cookie):
    headers = Auth().auth_valid_credential(get_header_cookie)
    id_non_existing_call = '111e1f1234818da20'
    url_delete = EndpointCalls.delete_call(id_non_existing_call)
    response_delete = EspoCRMRequest.delete(url_delete, headers)
    assert_status_code_not_found(response_delete)
    assert_delete_failed_response_message(response_delete)

@allure.suite('EspoCRM')
@allure.sub_suite('Alison')
@allure.epic('EspoCRM')
@allure.feature('Calls')
@allure.story('Delete Call')
@allure.tag('author: Alison')
@pytest.mark.functional
@pytest.mark.regression
# Verify deletion of a call with invalid ID format - status code 400 Bad Request
def test_delete_invalid_call_id(get_header_cookie):
    headers = Auth().auth_valid_credential(get_header_cookie)
    invalid_id_call = '*-/+-+!"#%##&/%$/'
    url_delete = EndpointCalls.delete_call(invalid_id_call)
    response_delete = EspoCRMRequest.delete(url_delete, headers)
    assert_status_bad_request(response_delete)
    assert_delete_failed_response_message(response_delete)

''' The result of this Test Case is a BUG, because instead of giving a status_code bad request, 
it returns a satus_code 200 ok'''

@allure.suite('EspoCRM')
@allure.sub_suite('Alison')
@allure.epic('EspoCRM')
@allure.feature('Calls')
@allure.story('Delete Call')
@allure.tag('author: Alison')
@pytest.mark.functional
@pytest.mark.regression
# Verify deletion of a call with invalid authorization cookie- status code 401 Unauthorized
def test_delete_call_with_invalid_cookie(setup_create_call, get_header_cookie):
    headers, id_of_new_call = setup_create_call
    print("This is the headers before: " + str(headers))
    invalid_cookie_header = deepcopy(headers)
    invalid_cookie_header['Cookie'] = 'auth-token-secret=wrong_secret; auth-token=wrong_token'
    print("This is the headers sent: " + str(invalid_cookie_header))

    url_delete = EndpointCalls.delete_call(id_of_new_call)
    response_delete = EspoCRMRequest.delete(url_delete, invalid_cookie_header)
    assert_status_code_unauthorized(response_delete)

    response_delete = EspoCRMRequest.delete(url_delete, headers)

@allure.suite('EspoCRM')
@allure.sub_suite('Alison')
@allure.epic('EspoCRM')
@allure.feature('Calls')
@allure.story('Delete Call')
@allure.tag('author: Alison')
@pytest.mark.functional
@pytest.mark.regression
# Verify deletion of  a call and check response content type - application/json
def test_delete_call_header_format_content_type(setup_create_call):
    headers, id_of_new_call = setup_create_call
    url_delete = EndpointCalls.delete_call(id_of_new_call)
    response_delete = EspoCRMRequest.delete(url_delete, headers)
    assert_content_type_application_json(response_delete)


