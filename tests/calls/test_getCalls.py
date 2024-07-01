import pytest
import requests

from config import BASE_URI, USERNAME, PASSWORD, CALL_PARAM
from conftest import encoded
from src.assertions.assertion_schemas import assert_schema_calls_without_filters
from src.assertions.assertion_response_data import assert_itemList_size_is_maxsize, \
    assert_list_acsOrder_with_OrderBy_Order_params, assert_offset_pagination_correctData
from src.assertions.assertion_schemas import assert_schema_call_with_specifiedFilters
from src.assertions.assertion_headers import assert_content_type_applicationJson
from src.assertions.assertion_status import assert_status_code_ok, assert_status_code_unauthorized, \
    assert_status_bad_request, assert_status_code_internal_server_error
from src.espocrm_api.api_request import EspoCRMRequest
from src.espocrm_api.calls_endpoints import EndpointCalls


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_get_calls_withNoParams_success(get_header_cookie):
    url = f"{BASE_URI}{EndpointCalls.GET_CALLS_WITHOUT_PARAMS.value}"
    response = EspoCRMRequest.get_with_url_headers(url, headers=get_header_cookie(USERNAME, PASSWORD))
    assert_status_code_ok(response)

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_get_calls_withNoParams_schema_validation(get_header_cookie):
    url = f"{BASE_URI}{EndpointCalls.GET_CALLS_WITHOUT_PARAMS.value}"
    response = EspoCRMRequest.get_with_url_headers(url, headers=get_header_cookie(USERNAME, PASSWORD))
    assert_schema_calls_without_filters(response.json())


@pytest.mark.functional
@pytest.mark.regression
def test_get_allCalls_withNoParams_format(get_header_cookie):
    url = f"{BASE_URI}{EndpointCalls.GET_CALLS_WITHOUT_PARAMS.value}"
    response = EspoCRMRequest.get_with_url_headers(url, headers=get_header_cookie(USERNAME, PASSWORD))
    assert_content_type_applicationJson(response)

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_get_calls_invalid_cookie_in_headers(get_header_cookie):
    url = f"{BASE_URI}{EndpointCalls.GET_CALLS_WITHOUT_PARAMS.value}"
    headers = get_header_cookie(USERNAME, PASSWORD)
    headers['Cookie'] = 'wrongCookie'
    response = EspoCRMRequest.get_with_url_headers(url, headers)
    assert_status_code_unauthorized(response)

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_get_calls_invalid_authorization_in_headers(get_header_cookie):
    url = f"{BASE_URI}{EndpointCalls.GET_CALLS_WITHOUT_PARAMS.value}"
    headers = get_header_cookie(USERNAME, PASSWORD)
    invalidAuth = encoded("invalidUser1232","invalidPassword456")
    headers['Authorization'] = 'Basic '+invalidAuth
    response = EspoCRMRequest.get_with_url_headers(url, headers)
    assert_status_code_unauthorized(response)

@pytest.mark.functional
@pytest.mark.regression
def test_get_calls_with_default_param(get_header_cookie):
    url = f"{BASE_URI}{EndpointCalls.GET_CALLS_WITH_PARAMS.value}"
    response = EspoCRMRequest.get_with_url_headers_params(url, params=CALL_PARAM, headers=get_header_cookie(USERNAME, PASSWORD))
    assert_status_code_ok(response)

@pytest.mark.functional
@pytest.mark.regression
def test_get_calls_with_param_select_otherValidData(get_header_cookie):
    url = f"{BASE_URI}{EndpointCalls.GET_CALLS_WITH_PARAMS.value}"
    selectData= "id%2Cname%2CcreatedById%2Cstatus"
    test_params = CALL_PARAM.copy()
    test_params['select'] = selectData
    response = EspoCRMRequest.get_with_url_headers_params(url, params=test_params, headers=get_header_cookie(USERNAME, PASSWORD))
    assert_status_code_ok(response)
    print("\n Response con filtros del get: \n"+str(response.json()))
    assert_schema_call_with_specifiedFilters(response.json(), selectData)
    '''
This assert fail because the response given doesn´t match the schema, there for its a BUG
    '''

@pytest.mark.functional
@pytest.mark.regression
def test_get_calls_with_param_select_invalidData(get_header_cookie):
    url = f"{BASE_URI}{EndpointCalls.GET_CALLS_WITH_PARAMS.value}"
    test_params = CALL_PARAM.copy()
    test_params['select'] = 'testCallsTest'
    response = EspoCRMRequest.get_with_url_headers_params(url, params=test_params, headers=get_header_cookie(USERNAME, PASSWORD))
    assert_status_bad_request(response)
    '''
This test case fails, and its correct because the field sent in 'select" doesn´t exist therefore 
it should return a bad request, but actually returns a status code 200
    '''

@pytest.mark.functional
@pytest.mark.regression
def test_get_calls_with_param_select_eliminated(get_header_cookie):
    url = f"{BASE_URI}{EndpointCalls.GET_CALLS_WITH_PARAMS.value}"
    test_params = CALL_PARAM.copy()
    if 'select' in test_params:
        del test_params['select']
    response = EspoCRMRequest.get_with_url_headers_params(url, params=test_params, headers=get_header_cookie(USERNAME, PASSWORD))
    assert_status_code_ok(response)
    assert_schema_calls_without_filters(response.json())

@pytest.mark.functional
@pytest.mark.regression
def test_get_calls_with_param_maxsize_otherValidData(get_header_cookie):
    url = f"{BASE_URI}{EndpointCalls.GET_CALLS_WITH_PARAMS.value}"
    test_params_maxsize_changed = CALL_PARAM.copy()
    test_params_maxsize_changed['maxSize'] = 1
    response = EspoCRMRequest.get_with_url_headers_params(url, params=test_params_maxsize_changed, headers=get_header_cookie(USERNAME, PASSWORD))
    assert_status_code_ok(response)
    assert_itemList_size_is_maxsize(response.json(), test_params_maxsize_changed['maxSize'])

@pytest.mark.functional
@pytest.mark.regression
def test_get_calls_with_param_maxsize_invalidData(get_header_cookie):
    url = f"{BASE_URI}{EndpointCalls.GET_CALLS_WITH_PARAMS.value}"
    test_params = CALL_PARAM.copy()
    test_params['maxsize'] = '2032+-*-/*-489589438345'
    response = EspoCRMRequest.get_with_url_headers_params(url, params=test_params, headers=get_header_cookie(USERNAME, PASSWORD))
    assert_status_bad_request(response)
    '''
This test case fails because the data sent in 'maxsize" invalid
therefore it should return a 400 bad request, but actually returns a status code 403 forbidden
     '''

@pytest.mark.functional
@pytest.mark.regression
def test_get_calls_with_param_maxsize_eliminated(get_header_cookie):
    url = f"{BASE_URI}{EndpointCalls.GET_CALLS_WITH_PARAMS.value}"
    test_params = CALL_PARAM.copy()
    if 'maxsize' in test_params:
        del test_params['maxsize']
    response = EspoCRMRequest.get_with_url_headers_params(url, params=test_params, headers=get_header_cookie(USERNAME, PASSWORD))
    assert_status_code_ok(response)

@pytest.mark.functional
@pytest.mark.regression
def test_get_calls_with_param_offset_otherValidData(get_header_cookie):
    url = f"{BASE_URI}{EndpointCalls.GET_CALLS_WITH_PARAMS.value}"
    test_params = CALL_PARAM.copy()
    response_without_offset = EspoCRMRequest.get_with_url_headers_params(url, params=test_params, headers=get_header_cookie(USERNAME, PASSWORD))

    offset = 1
    test_params_offset = CALL_PARAM.copy()
    test_params_offset['offset'] = offset
    response_with_offset = EspoCRMRequest.get_with_url_headers_params(url, params=test_params_offset, headers=get_header_cookie(USERNAME, PASSWORD))

    assert_status_code_ok(response_without_offset)
    assert_status_code_ok(response_with_offset)

    assert_offset_pagination_correctData(response_without_offset.json(), response_with_offset.json(), offset)

@pytest.mark.functional
@pytest.mark.regression
def test_get_calls_with_param_offset_invalidData(get_header_cookie):
    url = f"{BASE_URI}{EndpointCalls.GET_CALLS_WITH_PARAMS.value}"
    test_params = CALL_PARAM.copy()
    test_params['offset'] = 'lpo/*-!"$$/%&(//&)(%$$<<'
    response = EspoCRMRequest.get_with_url_headers_params(url, params=test_params, headers=get_header_cookie(USERNAME, PASSWORD))
    assert_status_bad_request(response)
'''
This test case fails, and its correct because the field sent in 'select" doesn´t exist therefore
it should return a bad request, but actually returns a status code 403
'''

@pytest.mark.functional
@pytest.mark.regression
def test_get_calls_with_param_offset_eliminated(get_header_cookie):
    url = f"{BASE_URI}{EndpointCalls.GET_CALLS_WITH_PARAMS.value}"
    test_params = CALL_PARAM.copy()
    if 'offset' in test_params:
        del test_params['offset']
    response = EspoCRMRequest.get_with_url_headers_params(url, params=test_params, headers=get_header_cookie(USERNAME, PASSWORD))
    assert_status_code_ok(response)

@pytest.mark.functional
@pytest.mark.regression
def test_get_calls_with_param_orderBy_and_order_otherValidData(get_header_cookie):
    url = f"{BASE_URI}{EndpointCalls.GET_CALLS_WITH_PARAMS.value}"
    test_params = CALL_PARAM.copy()
    test_params['orderBy'] = 'dateEnd'
    test_params['order'] = 'asc'
    response = EspoCRMRequest.get_with_url_headers_params(url, params=test_params, headers=get_header_cookie(USERNAME, PASSWORD))
    assert_status_code_ok(response)
    assert_list_acsOrder_with_OrderBy_Order_params(response.json())

@pytest.mark.functional
@pytest.mark.regression
def test_get_calls_with_param_orderBy_and_order_invalidData(get_header_cookie):
    url = f"{BASE_URI}{EndpointCalls.GET_CALLS_WITH_PARAMS.value}"
    test_params_change_orderBy = CALL_PARAM.copy()
    test_params_change_orderBy['orderBy'] = 'lpo/*-!"$$/%&(//&)(%$$<<'
    response = EspoCRMRequest.get_with_url_headers_params(url, params=test_params_change_orderBy, headers=get_header_cookie(USERNAME, PASSWORD))
    assert_status_bad_request(response)
    test_params_change_order = CALL_PARAM.copy()
    test_params_change_order['order']='-*/*-/*-/*-"!"#%%&(/%&%9'
    response = EspoCRMRequest.get_with_url_headers_params(url, params=test_params_change_order, headers=get_header_cookie(USERNAME, PASSWORD))
    assert_status_bad_request(response)

@pytest.mark.functional
@pytest.mark.regression
def test_get_calls_with_param_orderBy_eliminated(get_header_cookie):
    url = f"{BASE_URI}{EndpointCalls.GET_CALLS_WITH_PARAMS.value}"
    test_params = CALL_PARAM.copy()
    if 'orderBy' in test_params:
        del test_params['orderBy']
    response = EspoCRMRequest.get_with_url_headers_params(url, params=test_params, headers=get_header_cookie(USERNAME, PASSWORD))
    assert_status_code_ok(response)

@pytest.mark.functional
@pytest.mark.regression
def test_get_calls_with_param_order_eliminated(get_header_cookie):
    url = f"{BASE_URI}{EndpointCalls.GET_CALLS_WITH_PARAMS.value}"
    test_params = CALL_PARAM.copy()
    if 'order' in test_params:
        del test_params['order']
    response = EspoCRMRequest.get_with_url_headers_params(url, params=test_params, headers=get_header_cookie(USERNAME, PASSWORD))
    assert_status_code_ok(response)

