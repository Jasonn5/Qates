import pytest
import requests
from config.config import BASE_URI, USERNAME, PASSWORD
from api_endpoints.mail_draft_endpoints import EndpointEmail

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_delete_email_draft_success(get_headers, setup_email_draft):
    draft_id = setup_email_draft
    headers = get_headers(USERNAME, PASSWORD)

    # Probar la eliminación del borrador
    delete_url = f"{BASE_URI}{EndpointEmail.DELETE_EMAIL_DRAFT.value.format(id=draft_id)}"
    delete_response = requests.delete(delete_url, headers=headers)
    assert delete_response.status_code == 200

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_delete_email_draft_no_auth_header(setup_email_draft):
    draft_id = setup_email_draft
    headers_no_auth = {
        'Content-Type': 'application/json'
    }

    # Probar la eliminación del borrador sin header de autorización
    delete_url = f"{BASE_URI}{EndpointEmail.DELETE_EMAIL_DRAFT.value.format(id=draft_id)}"
    delete_response = requests.delete(delete_url, headers=headers_no_auth)
    assert delete_response.status_code == 401

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_delete_email_draft_invalid_auth_token(setup_email_draft):
    draft_id = setup_email_draft
    headers_invalid_auth = {
        'Authorization': 'Basic invalid_token',
        'Content-Type': 'application/json'
    }

    # Probar la eliminación del borrador con un token de autorización inválido
    delete_url = f"{BASE_URI}{EndpointEmail.DELETE_EMAIL_DRAFT.value.format(id=draft_id)}"
    delete_response = requests.delete(delete_url, headers=headers_invalid_auth)
    assert delete_response.status_code == 401

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_delete_email_draft_expired_auth_token(setup_email_draft):
    draft_id = setup_email_draft
    headers_expired_auth = {
        'Authorization': 'Basic expired_token',
        'Content-Type': 'application/json'
    }

    # Probar la eliminación del borrador con un token de autorización expirado (Simulado)
    delete_url = f"{BASE_URI}{EndpointEmail.DELETE_EMAIL_DRAFT.value.format(id=draft_id)}"
    delete_response = requests.delete(delete_url, headers=headers_expired_auth)
    assert delete_response.status_code == 401

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_delete_email_draft_response_content_type(get_headers, setup_email_draft):
    draft_id = setup_email_draft
    headers = get_headers(USERNAME, PASSWORD)

    # Probar la eliminación del borrador y verificar el tipo de contenido en la respuesta
    delete_url = f"{BASE_URI}{EndpointEmail.DELETE_EMAIL_DRAFT.value.format(id=draft_id)}"
    delete_response = requests.delete(delete_url, headers=headers)
    assert delete_response.status_code == 200
    assert delete_response.headers['Content-Type'] == 'application/json'
