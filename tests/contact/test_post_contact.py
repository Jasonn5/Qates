from api_endpoints.api_request import EspoCRMRequest
from api_endpoints.contact_endpoint import ContactEndpoint
from assertions.assertion_schemas import assert_schema_contact_post, assert_schema_error_contact_post
from assertions.assertion_status import assert_status_code_conflict, assert_status_code_created, \
    assert_status_bad_request
from config.config import BASE_URI
from payloads.contact.payload_contact import CONTACT_PAYLOAD
from payloads.contact.payload_contact_full_values import CONTACT_FULL_PAYLOAD
from tests.contact.conftest import modify_first_name_payload, teardown_post_contact

url = f"{BASE_URI}{ContactEndpoint.MAIN_ROUTE.value}?"
payload = CONTACT_PAYLOAD
full_payload = CONTACT_FULL_PAYLOAD


def test_post_contact_success(get_headers):
    payload['firstName'] = modify_first_name_payload()
    headers = get_headers("admin", "admin")
    response = EspoCRMRequest.post(url, headers=headers, payload=payload)
    response_json = response.json()
    assert_status_code_created(response)
    teardown_post_contact(get_headers, response_json['id'])


def test_contact_schema_validation(get_headers):
    payload['firstName'] = modify_first_name_payload()
    headers = get_headers("admin", "admin")
    response = EspoCRMRequest.post(url, headers=headers, payload=payload)
    assert_schema_contact_post(response.json())
    response_json = response.json()
    teardown_post_contact(get_headers, response_json)


def test_duplicate_contact(get_headers):
    payload['firstName'] = modify_first_name_payload()
    headers = get_headers("admin", "admin")
    EspoCRMRequest.post(url, headers=headers, payload=payload)
    duplicated_response = EspoCRMRequest.post(url, headers=headers, payload=payload)
    assert_status_code_conflict(duplicated_response)
    response_json = duplicated_response.json()
    teardown_post_contact(get_headers, response_json)


def test_required_first_name_empty(get_headers):
    payload['firstName'] = ""
    payload['lastName'] = modify_first_name_payload()
    headers = get_headers("admin", "admin")
    response = EspoCRMRequest.post(url, headers=headers, payload=payload)
    assert_status_bad_request(response)
    response_json = response.json()
    teardown_post_contact(get_headers, response_json)


def test_required_last_name_empty(get_headers):
    payload['firstName'] = modify_first_name_payload()
    payload['lastName'] = ""
    headers = get_headers("admin", "admin")
    response = EspoCRMRequest.post(url, headers=headers, payload=payload)
    assert_status_bad_request(response)
    response_json = response.json()
    teardown_post_contact(get_headers, response_json)


def test_error_contact_schema_validation(get_headers):
    payload['firstName'] = modify_first_name_payload()
    headers = get_headers("admin", "admin")
    response = EspoCRMRequest.post(url, headers=headers, payload=payload)
    assert_schema_error_contact_post(response.json())
    response_json = response.json()
    teardown_post_contact(get_headers, response_json)


def test_post_contact_success_with_all_values(get_headers):
    full_payload['firstName'] = modify_first_name_payload()
    headers = get_headers("admin", "admin")
    response = EspoCRMRequest.post(url, headers=headers, payload=payload)
    assert_status_code_created(response)
    response_json = response.json()
    teardown_post_contact(get_headers, response_json)
