import random
from api.request.api_request import EspoCRMRequest
from api.endpoints.contact import ContactEndpoint
from core.config.config import BASE_URI
from core.payloads.contact.payload_contact import CONTACT_PAYLOAD
from core.payloads.contact.payload_contact_full_values import CONTACT_FULL_PAYLOAD
from core.payloads.contact.payload_put_contact import CONTACT_PUT_PAYLOAD


START_RANDOM = 1
END_RANDOM = 100000
NAME_TEXT = "Michi"
url = f"{BASE_URI}{ContactEndpoint.MAIN_ROUTE.value}"

#put variables
put_payload = CONTACT_PUT_PAYLOAD
test_id = "668afc5b657557dfb"
put_url = f"{BASE_URI}{ContactEndpoint.MAIN_ROUTE.value}/{test_id}"
#post variables
post_payload = CONTACT_PAYLOAD
post_full_payload = CONTACT_FULL_PAYLOAD


def modify_first_name_payload():
    number = random.randint(START_RANDOM, END_RANDOM)
    return NAME_TEXT + str(number)


def teardown_post_contact(headers, response):
    contact_id = str(response['id'])
    delete_contact_url = f"{url}/{contact_id}"
    michi = EspoCRMRequest.delete(url=delete_contact_url, headers=headers)
    print("Michi")
