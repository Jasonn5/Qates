import pytest
import requests
from config.config import BASE_URI, EndpointEmail
import base64

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
    "status": "Draft",
    "subject": "No Subject",
    "to": ""
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
    "status": "Draft",
    "subject": "No Subject",
    "to": ""
}

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_create_email_draft_success(get_headers):
    url = f"{BASE_URI}{EndpointEmail['POST_EMAIL_DRAFT']}"
    headers = get_headers('admin', 'admin')
    print(f"Request Headers: {headers}")
    response = requests.post(url, headers=headers, json=payload_success)
    print(f"Response: {response.text}")
    assert response.status_code == 201

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_create_email_draft_missing_fields(get_headers):
    url = f"{BASE_URI}{EndpointEmail['POST_EMAIL_DRAFT']}"
    headers = get_headers('admin', 'admin')
    print(f"Request Headers: {headers}")
    response = requests.post(url, headers=headers, json={})
    print(f"Response: {response.text}")
    assert response.status_code == 400

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_create_email_draft_invalid_email_format(get_headers):
    url = f"{BASE_URI}{EndpointEmail['POST_EMAIL_DRAFT']}"
    headers = get_headers('admin', 'admin')
    print(f"Request Headers: {headers}")
    response = requests.post(url, headers=headers, json=payload_invalid_email_format)
    print(f"Response: {response.text}")
    assert response.status_code == 400
