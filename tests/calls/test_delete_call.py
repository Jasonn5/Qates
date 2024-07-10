import allure
import pytest

from api.request.api_request import EspoCRMRequest
from api.endpoints.calls import EndpointCalls
from core.assertions.calls import assert_delete_success_response_message, assert_delete_failed_response_message
from core.assertions.headers import assert_content_type_application_json
from core.assertions.status import assert_status_code_ok, assert_status_code_not_found, assert_status_bad_request, \
    assert_status_code_unauthorized
from tests.conftest import encoded
from resources.auth.auth import Auth


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_delete_call_successful(setup_create_call):
    headers, id_of_new_call = setup_create_call
    url_delete = EndpointCalls.delete_call(id_of_new_call)
    response_delete = EspoCRMRequest.delete(url_delete, headers)
    assert_status_code_ok(response_delete)
    assert_delete_success_response_message(response_delete)

@allure.feature('Calls - Alison Guzman')
@allure.story('Delete Calls')
@pytest.mark.functional
@pytest.mark.regression
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

@allure.feature('Calls - Alison Guzman')
@allure.story('Delete Calls')
@pytest.mark.functional
@pytest.mark.regression
def test_delete_call_header_format_content_type(setup_create_call):
    headers, id_of_new_call = setup_create_call
    url_delete = EndpointCalls.delete_call(id_of_new_call)
    response_delete = EspoCRMRequest.delete(url_delete, headers)
    assert_content_type_application_json(response_delete)

@allure.feature('Calls - Alison Guzman')
@allure.story('Delete Calls')
@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
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

@allure.feature('Calls - Alison Guzman')
@allure.story('Delete Calls')
@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_delete_unexisting_call(get_header_cookie):
    headers = Auth().auth_valid_credential(get_header_cookie)
    id_unexisting_call = '111e1f1234818da20'
    url_delete = EndpointCalls.delete_call(id_unexisting_call)
    response_delete = EspoCRMRequest.delete(url_delete, headers)
    assert_status_code_not_found(response_delete)
    assert_delete_failed_response_message(response_delete)

@allure.feature('Calls - Alison Guzman')
@allure.story('Delete Calls')
@pytest.mark.functional
@pytest.mark.regression
def test_delete_invalid_call_id(get_header_cookie):
    headers = Auth().auth_valid_credential(get_header_cookie)
    invalid_id_call = '*-/+-+!"#%##&/%$/'
    url_delete = EndpointCalls.delete_call(invalid_id_call)
    response_delete = EspoCRMRequest.delete(url_delete, headers)
    assert_status_bad_request(response_delete)
    assert_delete_failed_response_message(response_delete)

''' The result of this Test Case is a BUG, because instead of giving a status_code bad request, 
it returns a satus_code 200 ok'''

@allure.feature('Calls - Alison Guzman')
@allure.story('Delete Calls')
@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_delete_call_with_invalid_authentication(setup_create_call):
    headers, id_of_new_call = setup_create_call
    invalid_authorization_header = headers
    invalidAuth = encoded("invalidUser1232", "invalidPassword456")
    invalid_authorization_header['Authorization'] = 'Basic ' + invalidAuth

    url_delete = EndpointCalls.delete_call(id_of_new_call)
    response_delete = EspoCRMRequest.delete(url_delete, invalid_authorization_header)
    assert_status_code_unauthorized(response_delete)

    response_delete = EspoCRMRequest.delete(url_delete, headers)

@allure.feature('Calls - Alison Guzman')
@allure.story('Delete Calls')
@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_delete_call_with_invalid_cookie(setup_create_call):
    headers, id_of_new_call = setup_create_call
    invalid_cookie_headers = headers
    invalid_cookie_headers['Cookie'] = 'wrongCookie'

    url_delete = EndpointCalls.delete_call(id_of_new_call)
    response_delete = EspoCRMRequest.delete(url_delete, invalid_cookie_headers)
    assert_status_code_unauthorized(response_delete)

    response_delete = EspoCRMRequest.delete(url_delete, headers)




