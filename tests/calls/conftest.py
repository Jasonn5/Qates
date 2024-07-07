from api_endpoints.api_request import EspoCRMRequest
from api_endpoints.calls_endpoints import EndpointCalls
from config.config import USERNAME, PASSWORD


@staticmethod
def teardown_call(id_call, headers):
    url = f"{EndpointCalls.delete_call()}/{id_call}"
    delete_response = EspoCRMRequest.delete(url, headers)




