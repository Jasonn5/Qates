from api_endpoints.api_request import EspoCRMRequest
from api_endpoints.calls_endpoints import EndpointCalls
from config.config import USERNAME, PASSWORD
from payloads.calls.pyload_call import call_payload_required_data


@staticmethod
def teardown_call(id_call, headers):
    url = f"{EndpointCalls.delete_call()}/{id_call}"
    delete_response = EspoCRMRequest.delete(url, headers)
@staticmethod
def set_up_call(headers):
    url = EndpointCalls.post_call()
    payload = call_payload_required_data
    create_response = EspoCRMRequest.post(url, headers, payload)
    return create_response




