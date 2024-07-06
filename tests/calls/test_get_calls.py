import pytest

from config.config import BASE_URI, CALL_PARAM, USERNAME, PASSWORD
from tests.conftest import encoded
from assertions.assertion_schemas import assert_schema_calls_without_filters
from assertions.assertion_response_data import assert_itemList_size_is_maxsize, \
    assert_list_acsOrder_with_OrderBy_Order_params, assert_offset_pagination_correctData
from assertions.assertion_schemas import assert_schema_call_with_specifiedFilters
from assertions.assertion_headers import assert_content_type_application_json
from assertions.assertion_status import assert_status_code_ok, assert_status_code_unauthorized, \
    assert_status_bad_request
from api_endpoints.api_request import EspoCRMRequest
from api_endpoints.calls_endpoints import EndpointCalls


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
    Este error se encuentra reportado en el BUG-35
    '''

@pytest.mark.functional
@pytest.mark.regression
def test_get_calls_with_param_select_invalidData(get_header_cookie):
    url = f"{BASE_URI}{EndpointCalls.GET_CALLS_WITH_PARAMS.value}"
    test_params = CALL_PARAM.copy()
    test_params['select'] = '¡?=(¡)??578788787'
    response = EspoCRMRequest.get_with_url_headers_params(url, params=test_params, headers=get_header_cookie(USERNAME, PASSWORD))
    print("\n This is the status-code of the response: " + str(response.status_code))
    assert_status_bad_request(response)
    '''
    Este error se encuentra reportado en el BUG-31
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
    test_params['maxSize'] = '2032+-*-/*-489589438345'
    response = EspoCRMRequest.get_with_url_headers_params(url, params=test_params, headers=get_header_cookie(USERNAME, PASSWORD))
    print("\n This is the status-code of the response: " + str(response.status_code))
    assert_status_bad_request(response)
    '''
    Este error se encuentra reportado en el BUG-27
     '''

@pytest.mark.functional
@pytest.mark.regression
def test_get_calls_with_param_maxsize_eliminated(get_header_cookie):
    url = f"{BASE_URI}{EndpointCalls.GET_CALLS_WITH_PARAMS.value}"
    test_params = CALL_PARAM.copy()
    if 'maxSize' in test_params:
        del test_params['maxSize']
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
    test_params['offset'] = '0.2356-*/¡?¿'
    response = EspoCRMRequest.get_with_url_headers_params(url, params=test_params, headers=get_header_cookie(USERNAME, PASSWORD))
    print("\n This is the status-code of the response: " + str(response.status_code))
    assert_status_bad_request(response)
'''
Este error se encuentra reportado en el BUG-28 
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

