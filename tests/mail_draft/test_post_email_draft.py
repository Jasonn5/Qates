import pytest
import requests
from config.config import BASE_URI, USERNAME, PASSWORD
from api_endpoints.mail_draft_endpoints import EndpointEmail

def encoded(username, password):
    import base64
    credentials = f"{username}:{password}"
    encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
    return encoded_credentials

def get_headers(username, password):
    encoded_credentials = encoded(username, password)
    headers = {
        'Authorization': f'Basic {encoded_credentials}',
        'Content-Type': 'application/json'
    }
    return headers

# Helper function to delete drafts (if not already implemented)
def delete_draft(draft_id):
    url = f"{BASE_URI}{EndpointEmail.DELETE_EMAIL_DRAFT.value.format(id=draft_id)}"
    headers = get_headers(USERNAME, PASSWORD)
    response = requests.delete(url, headers=headers)
    return response

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_delete_email_draft_success():
    # Aquí deberías tener lógica para crear un borrador antes de intentar eliminarlo
    draft_id = 'valid_draft_id'  # Reemplazar con el ID del borrador válido creado
    response = delete_draft(draft_id)
    assert response.status_code == 200

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_delete_email_draft_no_auth_header():
    draft_id = 'valid_draft_id'  # Reemplazar con el ID del borrador válido creado
    url = f"{BASE_URI}{EndpointEmail.DELETE_EMAIL_DRAFT.value.format(id=draft_id)}"
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.delete(url, headers=headers)
    assert response.status_code == 401

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_delete_email_draft_invalid_auth_token():
    draft_id = 'valid_draft_id'  # Reemplazar con el ID del borrador válido creado
    url = f"{BASE_URI}{EndpointEmail.DELETE_EMAIL_DRAFT.value.format(id=draft_id)}"
    headers = {
        'Authorization': 'Basic invalid_token',
        'Content-Type': 'application/json'
    }
    response = requests.delete(url, headers=headers)
    assert response.status_code == 401

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_delete_email_draft_valid_cc_bcc():
    draft_id = 'valid_draft_id'  # Reemplazar con el ID del borrador válido creado
    url = f"{BASE_URI}{EndpointEmail.DELETE_EMAIL_DRAFT.value.format(id=draft_id)}"
    headers = get_headers(USERNAME, PASSWORD)
    response = delete_draft(draft_id)
    assert response.status_code == 200
    assert 'Content-Type' in response.headers
    assert response.headers['Content-Type'] == 'application/json'
