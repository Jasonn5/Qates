import json

import pytest
from api.request.api_request import EspoCRMRequest
from api.endpoints.calls import EndpointCalls
from core.payloads.calls.pyload_call import call_payload_required_data
from resources.auth.auth import Auth

@pytest.fixture(scope="module")
def base_payload_post():
    with open('core/payloads/calls/payload_call_data.json', 'r') as file:
        return json.load(file)

@pytest.fixture(scope="module")
def base_payload_delete():
    with open('core/payloads/calls/payload_delete_more_than_one_call.json', 'r') as file:
        return json.load(file)

@pytest.fixture(scope="function")
def teardown_delete_call(get_header_cookie):
    headers = Auth().auth_valid_credential(get_header_cookie)
    created_ids = []
    print("test initialized")
    yield created_ids
    for call_id in created_ids:
        delete_url = url = EndpointCalls.delete_call(call_id)
        EspoCRMRequest.delete(delete_url, headers)


@pytest.fixture(scope="function")
def setup_create_call(get_header_cookie, base_payload_post):
    headers = Auth().auth_valid_credential(get_header_cookie)
    url = EndpointCalls.post_call()
    create_response = EspoCRMRequest.post(url, headers, base_payload_post)
    call_id = create_response.json().get('id')

    yield headers, call_id


@pytest.fixture(scope="function")
def setup_create_call_get_response(get_header_cookie, base_payload_post):
    headers = Auth().auth_valid_credential(get_header_cookie)
    url = EndpointCalls.post_call()
    create_response = EspoCRMRequest.post(url, headers, base_payload_post)
    call_id = create_response.json().get('id')

    yield headers, call_id, create_response

@pytest.fixture(scope="function")
def setup_teardown_call(get_header_cookie, base_payload_post):
    headers = Auth().auth_valid_credential(get_header_cookie)
    url = EndpointCalls.post_call()
    response = EspoCRMRequest.post(url, headers, base_payload_post)
    call_id = response.json().get('id')

    yield headers, call_id

    delete_url = url = f"{EndpointCalls.delete_call()}/{call_id}"
    EspoCRMRequest.delete(delete_url, headers)





