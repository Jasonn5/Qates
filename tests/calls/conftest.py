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
    with open('payloads/calls/payload_delete_more_than_one_call.json', 'r') as file:
        return json.load(file)

#@staticmethod
def teardown_call(id_call, headers):
    url = f"{EndpointCalls.delete_call()}/{id_call}"
    delete_response = EspoCRMRequest.delete(url, headers)
#@staticmethod
def set_up_call(headers):
    url = EndpointCalls.post_call()
    payload = call_payload_required_data
    create_response = EspoCRMRequest.post(url, headers, payload)
    return create_response

@pytest.fixture(scope="function")
def setup_create_call(get_header_cookie):
    headers = Auth().auth_valid_credential(get_header_cookie)
    response = set_up_call(headers)
    call_id = response.json().get('id')

    yield headers, call_id, response





