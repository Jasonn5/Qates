import requests
import json
from config import BASE_URI
from src.resources.auth.auth import Auth
from src.espocrm_api.meetring_endpoints import EndpointMeetings


with open('src/payloads/meeting_payload.json', 'r') as file:
    BASE_PAYLOAD = json.load(file)

def create_meeting_with_payload(get_headers, payload_modification):
    url = f"{BASE_URI}{EndpointMeetings.CREATE_MEETING.value}"
    payload = BASE_PAYLOAD.copy()
    payload.update(payload_modification)
    headers = Auth().auth_valid_credential(get_headers)
    return requests.post(url, headers=headers, json=payload)


