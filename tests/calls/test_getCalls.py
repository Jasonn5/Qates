import pytest
import requests

from src.assertions.assertion_schemas import assert_schema_calls_without_params
from src.assertions.assert_headers import assert_content_type_applicationJson
from config import  BASE_URI, USERNAME, PASSWORD, calls_params
from conftest import encoded
from src.assertions.assertion_status import assert_status_code_ok, assert_status_code_unauthorized, \
    assert_status_bad_request, assert_status_code_internal_server_error


@pytest.mark.smoke
def test_get_allCalls_withNoParams_success(get_headers):
    url = f"{BASE_URI}/Call"
    response = requests.get(url, headers=get_headers(USERNAME, PASSWORD))
    assert_status_code_ok(response)

@pytest.mark.smoke
def test_get_calls_schema_validation(get_headers):
    url = f"{BASE_URI}/Call"
    response = requests.get(url, headers=get_headers(USERNAME, PASSWORD))
    headers = response.headers
    #print(headers.get('Content-Type'))
    assert_schema_calls_without_params(response.json())

def test_get_allCalls_withNoParams_format(get_headers):
    url = f"{BASE_URI}/Call"
    response = requests.get(url, headers=get_headers(USERNAME, PASSWORD))
    assert_content_type_applicationJson(response)

def test_get_calls_invalid_cookie_in_headers(get_header_cookie):
    url = f"{BASE_URI}/Call"
    #get_headers['Content-Type'] = 'ext/css'
    headers = get_header_cookie(USERNAME, PASSWORD)
    headers['Cookie'] = 'wrongCookie'
    response = requests.get(url, headers=headers)
    assert_status_code_unauthorized(response)

def test_get_calls_invalid_authorization_in_headers(get_header_cookie):
    url = f"{BASE_URI}/Call"
    headers = get_header_cookie(USERNAME, PASSWORD)
    invalidAuth = encoded("invalidUser1232","invalidPassword456")
    headers['Authorization'] = 'Basic '+invalidAuth
    response = requests.get(url, headers=headers)
    assert_status_code_unauthorized(response)

def test_get_calls_with_param_select_maxsize_offset_orderby_order_default(get_header_cookie):
    url = f"{BASE_URI}/Call?"
    headers = get_header_cookie(USERNAME, PASSWORD)
    response = requests.get(url, params=calls_params, headers=headers)
    assert_status_code_ok(response)

def test_get_calls_with_param_select_otherValidData(get_header_cookie):
    url = f"{BASE_URI}/Call?"
    headers = get_header_cookie(USERNAME, PASSWORD)
    calls_params['select'] = 'dateStart%2dateEnd%Cstatus%2Cname%Cid'
    response = requests.get(url, params=calls_params, headers=headers)
    assert_status_code_ok(response)

def test_get_calls_with_param_select_invalidData(get_header_cookie):
    url = f"{BASE_URI}/Call?"
    headers = get_header_cookie(USERNAME, PASSWORD)
    calls_params['select'] = 'testCallsTest'
    response = requests.get(url, params=calls_params, headers=headers)
    assert_status_bad_request(response)
    assert_status_code_internal_server_error(response)
    #This test case fails, and its correct because the field sent in 'select" doesn´t exist therefore
    # it should return a bad request, but actually returns a status code 200

def test_get_calls_with_param_select_empty(get_header_cookie):
    url = f"{BASE_URI}/Call?"
    headers = get_header_cookie(USERNAME, PASSWORD)
    response = requests.get(url, params=calls_params, headers=headers)
    if 'select' in calls_params:
        del calls_params['select']
    response = requests.get(url, params=calls_params, headers=headers)
    assert_status_code_ok(response)

def test_get_calls_with_param_maxsize_otherValidData(get_header_cookie):
    url = f"{BASE_URI}/Call?"
    headers = get_header_cookie(USERNAME, PASSWORD)
    calls_params['select'] = '1'
    response = requests.get(url, params=calls_params, headers=headers)
    assert_status_code_ok(response)

def test_get_calls_with_param_maxsize_invalidData(get_header_cookie):
    url = f"{BASE_URI}/Call?"
    headers = get_header_cookie(USERNAME, PASSWORD)
    calls_params['maxsize'] = ('2032+-*-/*-489589438345')
    response = requests.get(url, params=calls_params, headers=headers)
    assert_status_bad_request(response)
    assert_status_code_internal_server_error(response)
    #This test case fails, and its correct because the field sent in 'select" doesn´t exist therefore
    # it should return a bad request, but actually returns a status code 403

def test_get_calls_with_param_maxsize_empty(get_header_cookie):
    url = f"{BASE_URI}/Call?"
    headers = get_header_cookie(USERNAME, PASSWORD)
    response = requests.get(url, params=calls_params, headers=headers)
    if 'maxsize' in calls_params:
        del calls_params['maxsize']
    response = requests.get(url, params=calls_params, headers=headers)
    assert_status_code_ok(response)

def test_get_calls_with_param_offset_otherValidData(get_header_cookie):
    url = f"{BASE_URI}/Call?"
    headers = get_header_cookie(USERNAME, PASSWORD)
    calls_params['offset'] = '1'
    response = requests.get(url, params=calls_params, headers=headers)
    assert_status_code_ok(response)

def test_get_calls_with_param_offset_invalidData(get_header_cookie):
    url = f"{BASE_URI}/Call?"
    headers = get_header_cookie(USERNAME, PASSWORD)
    calls_params['offset'] = ('lpo/*-!"$$/%&(//&)(%$$<<')
    response = requests.get(url, params=calls_params, headers=headers)
    assert_status_bad_request(response)
    assert_status_code_internal_server_error(response)
    #This test case fails, and its correct because the field sent in 'select" doesn´t exist therefore
    # it should return a bad request, but actually returns a status code 403

def test_get_calls_with_param_offset_empty(get_header_cookie):
    url = f"{BASE_URI}/Call?"
    headers = get_header_cookie(USERNAME, PASSWORD)
    response = requests.get(url, params=calls_params, headers=headers)
    if 'offset' in calls_params:
        del calls_params['offset']
    response = requests.get(url, params=calls_params, headers=headers)
    assert_status_code_ok(response)

def test_get_calls_with_param_orderBy_otherValidData(get_header_cookie):
    url = f"{BASE_URI}/Call?"
    headers = get_header_cookie(USERNAME, PASSWORD)
    calls_params['orderBy'] = 'dateEnd'
    response = requests.get(url, params=calls_params, headers=headers)
    assert_status_code_ok(response)

def test_get_calls_with_param_orderBY_invalidData(get_header_cookie):
    url = f"{BASE_URI}/Call?"
    headers = get_header_cookie(USERNAME, PASSWORD)
    calls_params['orderBy'] = ('lpo/*-!"$$/%&(//&)(%$$<<')
    response = requests.get(url, params=calls_params, headers=headers)
    assert_status_bad_request(response)

def test_get_calls_with_param_orderBy_empty(get_header_cookie):
    url = f"{BASE_URI}/Call?"
    headers = get_header_cookie(USERNAME, PASSWORD)
    response = requests.get(url, params=calls_params, headers=headers)
    if 'orderBy' in calls_params:
        del calls_params['orderBy']
    response = requests.get(url, params=calls_params, headers=headers)
    assert_status_code_ok(response)

def test_get_calls_with_param_order_otherValidData(get_header_cookie):
    url = f"{BASE_URI}/Call?"
    headers = get_header_cookie(USERNAME, PASSWORD)
    calls_params['order'] = 'asc'
    response = requests.get(url, params=calls_params, headers=headers)
    assert_status_code_ok(response)

def test_get_calls_with_param_order_invalidData(get_header_cookie):
    url = f"{BASE_URI}/Call?"
    headers = get_header_cookie(USERNAME, PASSWORD)
    calls_params['order'] = ('lpo/*-!"$$/%&(//&)(%$$<<')
    response = requests.get(url, params=calls_params, headers=headers)

    assert_status_bad_request(response)

def test_get_calls_with_param_order_empty(get_header_cookie):
    url = f"{BASE_URI}/Call?"
    headers = get_header_cookie(USERNAME, PASSWORD)
    response = requests.get(url, params=calls_params, headers=headers)
    if 'order' in calls_params:
        del calls_params['order']
    response = requests.get(url, params=calls_params, headers=headers)
    assert_status_code_ok(response)
