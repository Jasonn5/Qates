import pytest

from api_endpoints.api_request import EspoCRMRequest
from api_endpoints.calls_endpoints import EndpointCalls
from assertions.assertion_status import assert_status_code_ok, assert_status_code_not_found, assert_status_bad_request, \
    assert_status_code_unauthorized
from config.config import USERNAME, PASSWORD
from tests.calls.conftest import set_up_call
from tests.conftest import encoded


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_delete_successful(get_header_cookie):
    headers = get_header_cookie(USERNAME, PASSWORD)
    response_set_up = set_up_call(headers)
    data_response = response_set_up.json()
    id_of_new_call = data_response["id"]
    url = f"{EndpointCalls.delete_call()}/{id_of_new_call}"
    response_delete = EspoCRMRequest.delete(url, headers)
    assert_status_code_ok(response_delete)

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

@pytest.mark.functional
@pytest.mark.regression
def test_delete_invalid_call(get_header_cookie):
    headers = get_header_cookie(USERNAME, PASSWORD)
    invalid_id_call = '*-/+-+!"#%##&/%$/'
    url = f"{EndpointCalls.delete_call()}/{invalid_id_call}"
    response_delete = EspoCRMRequest.delete(url, headers)
    assert_status_bad_request(response_delete)

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_delete_call_with_invalid_authentication(get_header_cookie):
    invalid_authentication_headers = get_header_cookie(USERNAME, PASSWORD)
    invalidAuth = encoded("invalidUser1232", "invalidPassword456")
    invalid_authentication_headers['Authorization'] = 'Basic ' + invalidAuth

    headers = get_header_cookie(USERNAME, PASSWORD)
    response_set_up = set_up_call(headers)
    data_response = response_set_up.json()
    id_of_new_call = data_response["id"]

    url = f"{EndpointCalls.delete_call()}/{id_of_new_call}"
    response_delete = EspoCRMRequest.delete(url, invalid_authentication_headers)
    assert_status_code_unauthorized(response_delete)

    response_delete = EspoCRMRequest.delete(url, headers)

def test_delete_call_with_invalid_cookie(get_header_cookie):
    invalid_headers = get_header_cookie(USERNAME, PASSWORD)
    invalid_headers['Cookie'] = 'wrongCookie'

    headers = get_header_cookie(USERNAME, PASSWORD)
    response_set_up = set_up_call(headers)
    data_response = response_set_up.json()
    id_of_new_call = data_response["id"]

    url = f"{EndpointCalls.delete_call()}/{id_of_new_call}"
    response_delete = EspoCRMRequest.delete(url, invalid_headers)
    assert_status_code_unauthorized(response_delete)

    response_delete = EspoCRMRequest.delete(url, headers)

def test_deleted_call_cannot_be_recovered(get_header_cookie):
   ''' invalid_headers = get_header_cookie(USERNAME, PASSWORD)
    invalid_headers['Cookie'] = 'wrongCookie'

    headers = get_header_cookie(USERNAME, PASSWORD)
    response_set_up = set_up_call(headers)
    data_response = response_set_up.json()
    id_of_new_call = data_response["id"]

    url = f"{EndpointCalls.delete_call()}/{id_of_new_call}"
    response_delete = EspoCRMRequest.delete(url, invalid_headers)
    assert_status_code_unauthorized(response_delete)

    response_delete = EspoCRMRequest.delete(url, headers)'''



