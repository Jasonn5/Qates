import random

from api_endpoints.api_request import EspoCRMRequest
from api_endpoints.contact_endpoint import ContactEndpoint
from assertions.assertion_status import assert_status_code_ok
from config.config import BASE_URI
from tests.conftest import get_headers

START_RANDOM = 1
END_RANDOM = 100000
NAME_TEXT = "Michi"
url = f"{BASE_URI}{ContactEndpoint.MAIN_ROUTE.value}"


def modify_first_name_payload():
    number = random.randint(START_RANDOM, END_RANDOM)
    return NAME_TEXT + str(number)


def teardown_post_contact(get_headers, response_json):
    contact_id = response_json['id']
    delete_contact_url = f"{url}/{contact_id}"
    headers = get_headers("admin", "admin")
    response = EspoCRMRequest.delete(delete_contact_url, headers=headers)

