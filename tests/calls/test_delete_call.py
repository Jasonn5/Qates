import pytest

from api_endpoints.api_request import EspoCRMRequest
from api_endpoints.calls_endpoints import EndpointCalls
from assertions.assertion_calls import assert_delete_success_response_message, assert_delete_failed_response_message
from assertions.assertion_headers import assert_content_type_application_json
from assertions.assertion_status import assert_status_code_ok, assert_status_code_not_found, assert_status_bad_request, \
    assert_status_code_unauthorized
from config.config import USERNAME, PASSWORD
from tests.calls.conftest import set_up_call
from tests.conftest import encoded


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_delete_call_successful(setup_create_call):
    headers, id_of_new_call, data_response = setup_create_call
    url_delete = f"{EndpointCalls.delete_call()}/{id_of_new_call}"
    response_delete = EspoCRMRequest.delete(url_delete, headers)
    assert_status_code_ok(response_delete)
    assert_delete_success_response_message(response_delete)

    '''url_get_by_id = f"{EndpointCalls.get_call_without_params()}/{id_of_new_call}"
    response_get_call_by_id = EspoCRMRequest.get_with_url_headers(url_get_by_id, headers)
    print("Status-code get unexisting call: "+ str(response_get_call_by_id.status_code))
    assert_status_code_not_found(response_get_call_by_id)'''

@pytest.mark.functional
@pytest.mark.regression
def test_delete_call_header_format_content_type(setup_create_call):
    headers, id_of_new_call, data_response = setup_create_call
    url_delete = f"{EndpointCalls.delete_call()}/{id_of_new_call}"
    response_delete = EspoCRMRequest.delete(url_delete, headers)
    assert_content_type_application_json(response_delete)

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_delete_more_than_one_call(get_header_cookie):
    url = EndpointCalls.delete_call()
    # This test case can't be executed because instead of using the verb DELETE to delete more than on call,
    # The system uses a POST, sending a body with the IDs of all the call to be eliminated

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_delete_unexisting_call(get_header_cookie):
    headers = get_header_cookie(USERNAME, PASSWORD)
    id_unexisting_call = '48923894oieopikrfjfw078754754454'
    url = f"{EndpointCalls.delete_call()}/{id_unexisting_call}"
    response_delete = EspoCRMRequest.delete(url, headers)
    assert_status_code_not_found(response_delete)
    assert_delete_failed_response_message(response_delete)

@pytest.mark.functional
@pytest.mark.regression
def test_delete_invalid_call_id(get_header_cookie):
    headers = get_header_cookie(USERNAME, PASSWORD)
    invalid_id_call = '*-/+-+!"#%##&/%$/'
    url = f"{EndpointCalls.delete_call()}/{invalid_id_call}"
    response_delete = EspoCRMRequest.delete(url, headers)
    assert_status_bad_request(response_delete)
    assert_delete_failed_response_message(response_delete)

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_delete_call_with_invalid_authentication(setup_create_call):
    headers, id_of_new_call, data_response = setup_create_call
    invalid_authorization_header = headers
    invalidAuth = encoded("invalidUser1232", "invalidPassword456")
    invalid_authorization_header['Authorization'] = 'Basic ' + invalidAuth


    url = f"{EndpointCalls.delete_call()}/{id_of_new_call}"
    response_delete = EspoCRMRequest.delete(url, invalid_authorization_header)
    assert_status_code_unauthorized(response_delete)

    response_delete = EspoCRMRequest.delete(url, headers)

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_delete_call_with_invalid_cookie(setup_create_call):
    headers, id_of_new_call, data_response = setup_create_call
    invalid_headers = headers
    invalid_headers['Cookie'] = 'wrongCookie'

    url = f"{EndpointCalls.delete_call()}/{id_of_new_call}"
    response_delete = EspoCRMRequest.delete(url, invalid_headers)
    assert_status_code_unauthorized(response_delete)

    response_delete = EspoCRMRequest.delete(url, headers)





