import requests
from config import BASE_URI
from src.assertions.assertion_status import (
    assert_status_code_ok,
    assert_status_code_unauthorized,
    assert_status_bad_request
)
from src.resources.auth.auth import Auth
from src.espocrm_api.email_endpoints import EndpointEmail

def test_get_email_succed(get_headers):
    url = f"{BASE_URI}{EndpointEmail.GET_EMAIL_WITHOUT_PARAMS.value}"
    response = requests.get(url, headers=Auth().auth_valid_credential(get_headers))
    assert_status_code_ok(response)

def test_get_all_drafts_status_code_200(get_headers):
    url = f"{BASE_URI}{EndpointEmail.GET_EMAIL_WITH_PARAMS.value}"
    headers = Auth().auth_valid_credential(get_headers)
    response = requests.get(url, headers=headers)
    assert_status_code_ok(response)

def test_get_drafts_with_wrong_basic_auth(get_headers):
    url = f"{BASE_URI}{EndpointEmail.GET_EMAIL_WITH_PARAMS.value}"
    headers = Auth().auth_invalid_credentials(get_headers)
    response = requests.get(url, headers=headers)
    assert_status_code_unauthorized(response)

def test_get_drafts_without_auth_token_secret(get_headers):
    url = f"{BASE_URI}{EndpointEmail.GET_EMAIL_WITH_PARAMS.value}"
    headers = Auth().auth_valid_credential(get_headers)
    if "cookie" in headers:
        headers.pop("cookie")
    response = requests.get(url, headers=headers)
    assert_status_code_unauthorized(response)

def test_get_drafts_with_wrong_content_type(get_headers):
    url = f"{BASE_URI}{EndpointEmail.GET_EMAIL_WITH_PARAMS.value}"
    headers = Auth().auth_valid_credential(get_headers)
    headers["Content-Type"] = "text/plain"
    response = requests.get(url, headers=headers)
    assert_status_bad_request(response)

def test_get_drafts_with_additional_parameters(get_headers):
    url = f"{BASE_URI}{EndpointEmail.GET_EMAIL_WITH_PARAMS.value}&extra_param=value"
    headers = Auth().auth_valid_credential(get_headers)
    response = requests.get(url, headers=headers)
    assert_status_bad_request(response)

def test_get_drafts_with_empty_search_param(get_headers):
    url = f"{BASE_URI}{EndpointEmail.GET_EMAIL_WITH_PARAMS.value}&search="
    headers = Auth().auth_valid_credential(get_headers)
    response = requests.get(url, headers=headers)
    assert_status_code_ok(response)

def test_get_drafts_with_invalid_search_fields(get_headers):
    url = f"{BASE_URI}{EndpointEmail.GET_EMAIL_WITH_PARAMS.value}&search=invalid_field"
    headers = Auth().auth_valid_credential(get_headers)
    response = requests.get(url, headers=headers)
    assert_status_bad_request(response)

def test_get_drafts_with_empty_maxsize_param(get_headers):
    url = f"{BASE_URI}{EndpointEmail.GET_EMAIL_WITH_PARAMS.value}&maxSize="
    headers = Auth().auth_valid_credential(get_headers)
    response = requests.get(url, headers=headers)
    assert_status_code_ok(response)

def test_get_drafts_with_valid_maxsize_param(get_headers):
    url = f"{BASE_URI}{EndpointEmail.GET_EMAIL_WITH_PARAMS.value}&maxSize=10"
    headers = Auth().auth_valid_credential(get_headers)
    response = requests.get(url, headers=headers)
    assert_status_code_ok(response)

def test_get_drafts_with_invalid_maxsize_param(get_headers):
    url = f"{BASE_URI}{EndpointEmail.GET_EMAIL_WITH_PARAMS.value}&maxSize=invalid"
    headers = Auth().auth_valid_credential(get_headers)
    response = requests.get(url, headers=headers)
    assert_status_bad_request(response)

def test_get_drafts_with_invalid_offset_type(get_headers):
    url = f"{BASE_URI}{EndpointEmail.GET_EMAIL_WITH_PARAMS.value}&offset=not_an_integer"
    headers = Auth().auth_valid_credential(get_headers)
    response = requests.get(url, headers=headers)
    assert_status_bad_request(response)

def test_get_drafts_with_invalid_order_type(get_headers):
    url = f"{BASE_URI}{EndpointEmail.GET_EMAIL_WITH_PARAMS.value}&order=invalid"
    headers = Auth().auth_valid_credential(get_headers)
    response = requests.get(url, headers=headers)
    assert_status_bad_request(response)
