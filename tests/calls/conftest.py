import pytest

from api_endpoints.api_request import EspoCRMRequest
from api_endpoints.calls_endpoints import EndpointCalls
from config.config import USERNAME, PASSWORD
from payloads.calls.pyload_call import call_payload_required_data


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
    headers = get_header_cookie(USERNAME, PASSWORD)
    response = set_up_call(headers)
    call_id = response.json().get('id')

    yield headers, call_id, response





