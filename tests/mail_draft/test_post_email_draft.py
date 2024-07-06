import pytest
import requests

from config.config import BASE_URI
from assertions.assertion_status import (
    assert_status_code_created,
    assert_status_bad_request
)
from resources.auth.auth import Auth
from api_endpoints.mail_draft_endpoints import EndpointEmail

# Data payload for creating email drafts
payload_success = {
    "status": "Draft",
    "isRead": True,
    "isImportant": False,
    "inTrash": False,
    "folderId": None,
    "isUsers": False,
    "attachmentsIds": [],
    "bcc": "",
    "body": None,
    "bodyPlain": None,
    "cc": "",
    "from": "hhellooworld01@gmail.com",
    "isHtml": True,
    "isJustSent": False,
    "isSystem": False,
    "name": "No Subject",
    "parentId": None,
    "parentName": None,
    "parentType": None,
    "selectTemplateId": None,
    "selectTemplateName": None,
    "subject": "No Subject",
    "to": ""
}

payload_missing_fields = {
    # Intentionally missing required fields
}

payload_invalid_email_format = {
    "status": "Draft",
    "isRead": True,
    "isImportant": False,
    "inTrash": False,
    "folderId": None,
    "isUsers": False,
    "attachmentsIds": [],
    "bcc": "",
    "body": None,
    "bodyPlain": None,
    "cc": "",
    "from": "invalid-email-format",
    "isHtml": True,
    "isJustSent": False,
    "isSystem": False,
    "name": "No Subject",
    "parentId": None,
    "parentName": None,
    "parentType": None,
    "selectTemplateId": None,
    "selectTemplateName": None,
    "subject": "No Subject",
    "to": ""
}

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_create_email_draft_success(get_headers):
    url = f"{BASE_URI}{EndpointEmail.POST_EMAIL_DRAFT.value}"
    headers = Auth().auth_valid_credential(get_headers)
    response = requests.post(url, headers=headers, json=payload_success)
    print(f"Response: {response.json()}")
    assert_status_code_created(response)

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_create_email_draft_missing_fields(get_headers):
    url = f"{BASE_URI}{EndpointEmail.POST_EMAIL_DRAFT.value}"
    headers = Auth().auth_valid_credential(get_headers)
    response = requests.post(url, headers=headers, json=payload_missing_fields)
    print(f"Response: {response.json()}")
    assert_status_bad_request(response)

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_create_email_draft_invalid_email_format(get_headers):
    url = f"{BASE_URI}{EndpointEmail.POST_EMAIL_DRAFT.value}"
    headers = Auth().auth_valid_credential(get_headers)
    response = requests.post(url, headers=headers, json=payload_invalid_email_format)
    print(f"Response: {response.json()}")
    assert_status_bad_request(response)
