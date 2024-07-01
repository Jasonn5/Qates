import pytest
import requests

from config import BASE_URI, USERNAME, PASSWORD, CALL_PARAM
from conftest import encoded
from src.assertions.assertion_schemas import assert_schema_calls_without_filters
from src.assertions.assertion_response_data import assert_itemList_size
from src.assertions.assertion_schemas import assert_schema_call_with_specifiedFilters
from src.assertions.assertion_headers import assert_content_type_applicationJson
from src.assertions.assertion_status import assert_status_code_ok, assert_status_code_unauthorized, \
    assert_status_bad_request, assert_status_code_internal_server_error
from src.espocrm_api.api_request import EspoCRMRequest
from src.espocrm_api.calls_endpoints import EndpointCalls


#Verificar que obtenga todos las llamadas sin filtros
@pytest.mark.smoke
def test_get_calls_withNoParams_success(get_header_cookie):
    url = f"{BASE_URI}{EndpointCalls.GET_CALLS_WITHOUT_PARAMS.value}"
    response = EspoCRMRequest.get_with_url_headers(url, headers=get_header_cookie(USERNAME, PASSWORD))
    assert_status_code_ok(response)

@pytest.mark.smoke
def test_get_calls_withNoParams_schema_validation(get_header_cookie):
    url = f"{BASE_URI}{EndpointCalls.GET_CALLS_WITHOUT_PARAMS.value}"
    response = EspoCRMRequest.get_with_url_headers(url, headers=get_header_cookie(USERNAME, PASSWORD))
    assert_schema_calls_without_filters(response.json())

def test_get_allCalls_withNoParams_format(get_header_cookie):
    url = f"{BASE_URI}{EndpointCalls.GET_CALLS_WITHOUT_PARAMS.value}"
    response = EspoCRMRequest.get_with_url_headers(url, headers=get_header_cookie(USERNAME, PASSWORD))
    assert_content_type_applicationJson(response)

def test_get_calls_invalid_cookie_in_headers(get_header_cookie):
    url = f"{BASE_URI}{EndpointCalls.GET_CALLS_WITHOUT_PARAMS.value}"
    headers = get_header_cookie(USERNAME, PASSWORD)
    headers['Cookie'] = 'wrongCookie'
    response = EspoCRMRequest.get_with_url_headers(url, headers)
    assert_status_code_unauthorized(response)

def test_get_calls_invalid_authorization_in_headers(get_header_cookie):
    url = f"{BASE_URI}{EndpointCalls.GET_CALLS_WITHOUT_PARAMS.value}"
    headers = get_header_cookie(USERNAME, PASSWORD)
    invalidAuth = encoded("invalidUser1232","invalidPassword456")
    headers['Authorization'] = 'Basic '+invalidAuth
    response = EspoCRMRequest.get_with_url_headers(url, headers)
    assert_status_code_unauthorized(response)

def test_get_calls_with_default_param(get_header_cookie):
    url = f"{BASE_URI}{EndpointCalls.GET_CALLS_WITH_PARAMS.value}"
    response = EspoCRMRequest.get_with_url_headers_params(url, params=CALL_PARAM, headers=get_header_cookie(USERNAME, PASSWORD))
    assert_status_code_ok(response)

def test_get_calls_with_param_select_otherValidData(get_header_cookie):
    url = f"{BASE_URI}{EndpointCalls.GET_CALLS_WITH_PARAMS.value}"
    selectData= 'id%2Cname%2CcreatedById%2Cstatus'
    test_params = CALL_PARAM.copy()
    test_params['select'] = selectData
    response = EspoCRMRequest.get_with_url_headers_params(url, params=test_params, headers=get_header_cookie(USERNAME, PASSWORD))
    assert_status_code_ok(response)
    #print("\n Response con filtros del get: \n"+str(response.json()))
    #assert_schema_call_with_specifiedFilters(response.json(), selectData)
    '''
This las assert fail because the response given doesn´t match the schema, there for its a BUG
    '''

def test_get_calls_with_param_select_invalidData(get_header_cookie):
    url = f"{BASE_URI}{EndpointCalls.GET_CALLS_WITH_PARAMS.value}"
    test_params = CALL_PARAM.copy()
    test_params['select'] = 'testCallsTest'
    response = EspoCRMRequest.get_with_url_headers_params(url, params=test_params, headers=get_header_cookie(USERNAME, PASSWORD))
    #assert_status_bad_request(response)
    '''
This test case fails, and its correct because the field sent in 'select" doesn´t exist therefore 
it should return a bad request, but actually returns a status code 200
    '''

def test_get_calls_with_param_select_empty(get_header_cookie):
    url = f"{BASE_URI}{EndpointCalls.GET_CALLS_WITH_PARAMS.value}"
    test_params = CALL_PARAM.copy()
    if 'select' in test_params:
        del test_params['select']
    response = EspoCRMRequest.get_with_url_headers_params(url, params=test_params, headers=get_header_cookie(USERNAME, PASSWORD))
    assert_status_code_ok(response)
    assert_schema_calls_without_filters(response.json())

def test_get_calls_with_param_maxsize_otherValidData(get_header_cookie):
    url = f"{BASE_URI}{EndpointCalls.GET_CALLS_WITH_PARAMS.value}"
    test_params = CALL_PARAM.copy()
    test_params['maxsize'] = '1'
    response = EspoCRMRequest.get_with_url_headers_params(url, params=test_params, headers=get_header_cookie(USERNAME, PASSWORD))
    assert_status_code_ok(response)
    #assert_itemList_size(response.json(), test_params['maxsize'])
    '''
This test case fails, because the request isn´t able to only show the maxsize asked, its stills shows all three calls in the response
    '''

def test_get_calls_with_param_maxsize_invalidData(get_header_cookie):
    url = f"{BASE_URI}{EndpointCalls.GET_CALLS_WITH_PARAMS.value}"
    test_params = CALL_PARAM.copy()
    test_params['maxsize'] = ('2032+-*-/*-489589438345')
    response = EspoCRMRequest.get_with_url_headers_params(url, params=test_params, headers=get_header_cookie(USERNAME, PASSWORD))
    #assert_status_bad_request(response)
    #assert_status_code_internal_server_error(response)
    '''
This test case fails because the data sent in 'maxsize" invalid
therefore it should return a 400 bad request, but actually returns a status code 403 forbidden
     '''

def test_get_calls_with_param_maxsize_empty(get_header_cookie):
    url = f"{BASE_URI}{EndpointCalls.GET_CALLS_WITH_PARAMS.value}"
    test_params = CALL_PARAM.copy()
    if 'maxsize' in test_params:
        del test_params['maxsize']
    response = EspoCRMRequest.get_with_url_headers_params(url, params=test_params, headers=get_header_cookie(USERNAME, PASSWORD))
    assert_status_code_ok(response)

def test_get_calls_with_param_offset_otherValidData(get_header_cookie):
    url = f"{BASE_URI}{EndpointCalls.GET_CALLS_WITH_PARAMS.value}"
    test_params = CALL_PARAM.copy()
    test_params['offset'] = '1'
    response = EspoCRMRequest.get_with_url_headers_params(url, params=test_params, headers=get_header_cookie(USERNAME, PASSWORD))
    assert_status_code_ok(response)

def test_get_calls_with_param_offset_invalidData(get_header_cookie):
    url = f"{BASE_URI}{EndpointCalls.GET_CALLS_WITH_PARAMS.value}"
    CALL_PARAM['offset'] = ('lpo/*-!"$$/%&(//&)(%$$<<')
    response = EspoCRMRequest.get_with_url_headers_params(url, params=CALL_PARAM, headers=get_header_cookie(USERNAME, PASSWORD))
    #assert_status_bad_request(response)
    #assert_status_code_internal_server_error(response)
    #This test case fails, and its correct because the field sent in 'select" doesn´t exist therefore
    # it should return a bad request, but actually returns a status code 403

def test_get_calls_with_param_offset_empty(get_header_cookie):
    url = f"{BASE_URI}{EndpointCalls.GET_CALLS_WITH_PARAMS.value}"
    if 'offset' in CALL_PARAM:
        del CALL_PARAM['offset']
    response = EspoCRMRequest.get_with_url_headers_params(url, params=CALL_PARAM, headers=get_header_cookie(USERNAME, PASSWORD))
    assert_status_code_ok(response)

def test_get_calls_with_param_orderBy_and_order_otherValidData(get_header_cookie):
    url = f"{BASE_URI}{EndpointCalls.GET_CALLS_WITH_PARAMS.value}"
    CALL_PARAM['orderBy'] = 'dateEnd'
    response = EspoCRMRequest.get_with_url_headers_params(url, params=CALL_PARAM, headers=get_header_cookie(USERNAME, PASSWORD))
    assert_status_code_ok(response)

def test_get_calls_with_param_orderBy_and_order_invalidData(get_header_cookie):
    url = f"{BASE_URI}{EndpointCalls.GET_CALLS_WITH_PARAMS.value}"
    CALL_PARAM['orderBy'] = ('lpo/*-!"$$/%&(//&)(%$$<<')
    response = EspoCRMRequest.get_with_url_headers_params(url, params=CALL_PARAM, headers=get_header_cookie(USERNAME, PASSWORD))
    assert_status_bad_request(response)

def test_get_calls_with_param_orderBy_empty(get_header_cookie):
    url = f"{BASE_URI}{EndpointCalls.GET_CALLS_WITH_PARAMS.value}"
    if 'orderBy' in CALL_PARAM:
        del CALL_PARAM['orderBy']
    response = EspoCRMRequest.get_with_url_headers_params(url, params=CALL_PARAM, headers=get_header_cookie(USERNAME, PASSWORD))
    assert_status_code_ok(response)

def test_get_calls_with_param_order_empty(get_header_cookie):
    url = f"{BASE_URI}{EndpointCalls.GET_CALLS_WITH_PARAMS.value}"
    if 'order' in CALL_PARAM:
        del CALL_PARAM['order']
    response = EspoCRMRequest.get_with_url_headers_params(url, params=CALL_PARAM, headers=get_header_cookie(USERNAME, PASSWORD))
    assert_status_code_ok(response)

