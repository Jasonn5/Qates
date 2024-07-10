'''import pytest
import requests

from core.config.config import BASE_URI
from core.assertions.status import (
    assert_status_code_ok,
    assert_status_code_unauthorized,
    assert_status_bad_request
)
from resources.auth.auth import Auth
from api.endpoints.mail_draft import EndpointEmail
from core.assertions.headers import assert_content_type_application_json

@pytest.mark.smoke
@pytest.mark.functional
def test_get_email_succed(get_headers):
    url = f"{BASE_URI}{EndpointEmail.GET_EMAIL_WITHOUT_PARAMS.value}"
    headers = Auth().auth_valid_credential(get_headers)
    response = requests.get(url, headers=headers)
    assert_status_code_ok(response)

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_get_all_drafts_status_code_200(get_headers):
    url = f"{BASE_URI}{EndpointEmail.GET_EMAIL_WITH_PARAMS.value}"
    headers = Auth().auth_valid_credential(get_headers)
    response = requests.get(url, headers=headers)
    assert_status_code_ok(response)

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_get_drafts_with_wrong_basic_auth(get_headers):
    url = f"{BASE_URI}{EndpointEmail.GET_EMAIL_WITH_PARAMS.value}"
    headers = Auth().auth_invalid_credentials(get_headers)
    response = requests.get(url, headers=headers)
    assert_status_code_unauthorized(response)

    Este error se encuentra reportado en el BUG-45


@pytest.mark.functional
@pytest.mark.regression
def test_get_drafts_without_auth_token_secret(get_headers):
    url = f"{BASE_URI}{EndpointEmail.GET_EMAIL_WITH_PARAMS.value}"
    headers = Auth().auth_valid_credential(get_headers)
    if "Cookie" in headers:
        del headers["Cookie"]
    response = requests.get(url, headers=headers)
    assert_status_code_unauthorized(response)

    Este error se encuentra reportado en el BUG-44


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_get_drafts_with_wrong_content_type(get_headers):
    url = f"{BASE_URI}{EndpointEmail.GET_EMAIL_WITH_PARAMS.value}"
    headers = Auth().auth_valid_credential(get_headers)
    headers["Content-Type"] = "text/plain"
    response = requests.get(url, headers=headers)
    assert_status_bad_request(response)

    Este error se encuentra reportado en el BUG-40


@pytest.mark.functional
@pytest.mark.regression
def test_get_drafts_with_additional_parameters(get_headers):
    url = f"{BASE_URI}{EndpointEmail.GET_EMAIL_WITH_PARAMS.value}&extra_param=value"
    headers = Auth().auth_valid_credential(get_headers)
    response = requests.get(url, headers=headers)
    assert_status_bad_request(response)

@pytest.mark.functional
@pytest.mark.regression
def test_get_drafts_with_empty_search_param(get_headers):
    url = f"{BASE_URI}{EndpointEmail.GET_EMAIL_WITH_PARAMS.value}&search="
    headers = Auth().auth_valid_credential(get_headers)
    response = requests.get(url, headers=headers)
    assert_status_code_ok(response)

    Este error se encuentra reportado en el BUG-43


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_get_drafts_with_invalid_search_fields(get_headers):
    url = f"{BASE_URI}{EndpointEmail.GET_EMAIL_WITH_PARAMS.value}&search=invalid_field"
    headers = Auth().auth_valid_credential(get_headers)
    response = requests.get(url, headers=headers)
    assert_status_bad_request(response)

@pytest.mark.functional
@pytest.mark.regression
def test_get_drafts_with_empty_maxsize_param(get_headers):
    url = f"{BASE_URI}{EndpointEmail.GET_EMAIL_WITH_PARAMS.value}&maxSize="
    headers = Auth().auth_valid_credential(get_headers)
    response = requests.get(url, headers=headers)
    assert_status_code_ok(response)

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_get_drafts_with_valid_maxsize_param(get_headers):
    url = f"{BASE_URI}{EndpointEmail.GET_EMAIL_WITH_PARAMS.value}&maxSize=10"
    headers = Auth().auth_valid_credential(get_headers)
    response = requests.get(url, headers=headers)
    assert_status_code_ok(response)

    Este error se encuentra reportado en el BUG-41


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_get_drafts_with_invalid_maxsize_param(get_headers):
    url = f"{BASE_URI}{EndpointEmail.GET_EMAIL_WITH_PARAMS.value}&maxSize=invalid"
    headers = Auth().auth_valid_credential(get_headers)
    response = requests.get(url, headers=headers)
    assert_status_bad_request(response)

    Este error se encuentra reportado en el BUG-42


@pytest.mark.functional
@pytest.mark.regression
def test_get_drafts_with_invalid_offset_type(get_headers):
    url = f"{BASE_URI}{EndpointEmail.GET_EMAIL_WITH_PARAMS.value}&offset=not_an_integer"
    headers = Auth().auth_valid_credential(get_headers)
    response = requests.get(url, headers=headers)
    assert_status_bad_request(response)

@pytest.mark.functional
@pytest.mark.regression
def test_get_drafts_with_invalid_order_type(get_headers):
    url = f"{BASE_URI}{EndpointEmail.GET_EMAIL_WITH_PARAMS.value}&order=invalid"
    headers = Auth().auth_valid_credential(get_headers)
    response = requests.get(url, headers=headers)
    assert_status_bad_request(response)

    Este error se encuentra reportado en el BUG-46


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_search_term_present_in_drafts(get_headers):
    url = f"{BASE_URI}{EndpointEmail.GET_EMAIL_WITH_PARAMS.value}&search=Luis"
    headers = Auth().auth_valid_credential(get_headers)
    response = requests.get(url, headers=headers)
    assert_status_code_ok(response)
    data = response.json()
    for item in data['list']:
        assert "Luis" in item['subject'] or "Luis" in item['personStringData']

@pytest.mark.functional
@pytest.mark.regression
def test_search_partial_term_in_drafts(get_headers):
    url = f"{BASE_URI}{EndpointEmail.GET_EMAIL_WITH_PARAMS.value}&search=Lu"
    headers = Auth().auth_valid_credential(get_headers)
    response = requests.get(url, headers=headers)
    assert_status_code_ok(response)
    data = response.json()
    for item in data['list']:
        assert "Lu" in item['subject'] or "Lu" in item['personStringData'], f"Expected 'Lu' in subject or personStringData, but got {item}"

@pytest.mark.functional
@pytest.mark.regression
def test_search_no_term_present_in_drafts(get_headers):
    url = f"{BASE_URI}{EndpointEmail.GET_EMAIL_WITH_PARAMS.value}&search="
    headers = Auth().auth_valid_credential(get_headers)
    response = requests.get(url, headers=headers)
    assert_status_code_ok(response)
    data = response.json()
    assert len(data['list']) == 0, f"Expected 0 results, but got {len(data['list'])}. Data: {data['list']}"

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_response_format_application_json(get_headers):
    url = f"{BASE_URI}{EndpointEmail.GET_EMAIL_WITH_PARAMS.value}"
    headers = Auth().auth_valid_credential(get_headers)
    response = requests.get(url, headers=headers)
    assert_content_type_application_json(response)'''
