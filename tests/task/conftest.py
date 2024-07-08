import pytest
import requests

from api_endpoints.task_ednpoints import TaskEnpoints
from api_endpoints.api_request import EspoCRMRequest
from resources.auth.auth import Auth


def create_task(get_headers, payload_task):
    url = TaskEnpoints.post_task_without_params()
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.post(url, headers, payload_task)
    return response.json()


def delete_task(task_id, get_headers):
    delete_url = f"{TaskEnpoints.post_task_without_params()}/{task_id}"
    headers = Auth().auth_valid_credential(get_headers)
    EspoCRMRequest.delete(delete_url, headers)

@pytest.fixture(scope="function")
def setup_teardown_task(get_headers, payload_task):
    url = TaskEnpoints.post_task_without_params()
    headers = Auth().auth_valid_credential(get_headers)
    response1 = requests.post(url, headers, payload_task)
    second_payload = response1.json()
    response2 = requests.post(url, headers, second_payload)

    yield response2

    task_id1 = response1.json().get('id')
    delete_task(task_id1, get_headers)

