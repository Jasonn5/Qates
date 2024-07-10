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
    headers = Auth().auth_valid_credential(get_header_cookie)
    id_unexisting_call = '48923894oieopikrfjfw078754754454'
    url = f"{EndpointCalls.delete_call()}/{id_unexisting_call}"
    response_delete = EspoCRMRequest.delete(url, headers)
    assert_status_code_not_found(response_delete)
    assert_delete_failed_response_message(response_delete)

@pytest.mark.functional
@pytest.mark.regression
def test_delete_invalid_call_id(get_header_cookie):
    headers = Auth().auth_valid_credential(get_header_cookie)
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
    invalid_authorization_header = Auth().auth_invalid_credentials(headers)
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





