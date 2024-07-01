import pytest
import requests
import base64

from config import BASE_URI, USERNAME, PASSWORD
from src.assertions.assertion_schemas import assert_schema_correoImportant
from src.assertions.assertion_headers import assert_content_type_applicationJson
from src.assertions.assertion_status import assert_status_code_ok, assert_status_code_unauthorized, assert_status_bad_request
from src.espocrm_api.api_request import EspoCRMRequest
from src.espocrm_api.correo_important_endpoint import EndpointCorreoImportant

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_get_email_success(get_headers):
    """
    Verificar que obtenga todos los mensajes marcados como Importantes - Status code 200 OK
    """
    url = f"{BASE_URI}{EndpointCorreoImportant.GET_CORREO_IMPORTANT.value}"
    headers = get_headers(USERNAME, PASSWORD)
    response = EspoCRMRequest.get_with_url_headers(url, headers)
    assert_status_code_ok(response)

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_get_email_schema_validation(get_headers):
    """
    Verificar que el parámetro 'select' contenga algunos campos válidos - Status code 200 OK
    """
    url = f"{BASE_URI}{EndpointCorreoImportant.GET_CORREO_IMPORTANT.value}"
    response = requests.get(url, headers=get_headers(USERNAME, PASSWORD))
    print("\n reponce del Get de correos \n" + str(response.json()))
    assert_schema_correoImportant(response.json())

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_get_email_response_format(get_headers):
    """
    Verificar que el formato de la respuesta sea 'application/json'
    """
    url = f"{BASE_URI}{EndpointCorreoImportant.GET_CORREO_IMPORTANT.value}"
    response = requests.get(url, headers=get_headers(USERNAME, PASSWORD))
    assert_content_type_applicationJson(response)

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_get_email_invalid_authorization_in_headers(get_header_cookie):
    """
    Verificar que el header tenga una BasicAuthorization errónea - Status code 401 Unauthorized
    """
    url = f"{BASE_URI}{EndpointCorreoImportant.GET_CORREO_IMPORTANT.value}"
    headers = get_header_cookie(USERNAME, PASSWORD)
    invalidAuth = base64.b64encode(b"invalidUser1232:invalidPassword456").decode('utf-8')
    headers['Authorization'] = 'Basic ' + invalidAuth
    response = requests.get(url, headers=headers)
    assert_status_code_unauthorized(response)

@pytest.mark.functional
@pytest.mark.regression
def test_get_email_invalid_cookie_in_headers(get_header_cookie):
    """
    Verificar que el header tenga una cookie sin auth-token-secret - Status code 401 Unauthorized
    """
    url = f"{BASE_URI}{EndpointCorreoImportant.GET_CORREO_IMPORTANT.value}"
    headers = get_header_cookie(USERNAME, PASSWORD)
    headers['Cookie'] = 'wrongCookie'
    response = requests.get(url, headers=headers)
    assert_status_code_unauthorized(response)

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_get_mail_valid_offset_parameter(get_headers):
    """
    Verificar que el parámetro 'offset' tenga un valor máximo válido - Status code 200 OK
    """
    url = f"{BASE_URI}{EndpointCorreoImportant.GET_CORREO_OFFSET_1000.value}"
    response = requests.get(url, headers=get_headers("admin", "admin"))
    assert_status_code_ok(response)

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_get_mail_valid_maxsize_parameter(get_headers):
    """
    Verificar que el parámetro 'maxsize' tenga un valor mínimo válido - Status code 200 OK
    """
    url = f"{BASE_URI}{EndpointCorreoImportant.GET_CORREO_MAXSIZE_1.value}"
    response = requests.get(url, headers=get_headers("admin", "admin"))
    assert_status_code_ok(response)

@pytest.mark.functional
@pytest.mark.regression
def test_get_mail_invalid_order_parameter(get_headers):
    """
    Verificar que el parámetro 'order' contenga valores numéricos/booleanos/strings - Status code 400 Bad Request
    """
    url = f"{BASE_URI}{EndpointCorreoImportant.GET_CORREO_INVALID_ORDER.value}"
    response = requests.get(url, headers=get_headers("admin", "admin"))
    assert response.status_code == 400

@pytest.mark.functional
@pytest.mark.regression
def test_get_mail_missing_auth_token_secret():
    """
    Verificar que el header tenga una cookie sin auth-token-secret - Status code 401 Unauthorized
    """
    url = f"{BASE_URI}/Email"
    headers = {"Cookie": "some_other_cookie=some_value"}
    response = requests.get(url, headers=headers)
    assert_status_code_unauthorized(response)

@pytest.mark.regression
def test_get_mail_invalid_basic_authorization():
    """
    Verificar que el header tenga una cookie sin auth-token-secret - Status code 401 Unauthorized
    """
    url = f"{BASE_URI}/Email"
    headers = {"Authorization": "Basic invalidcredentials"}
    response = requests.get(url, headers=headers)
    assert_status_code_unauthorized(response)