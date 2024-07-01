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
def test_get_email_success(get_headers):
    # Prueba que verifica si se pueden obtener correos que son importantes exitosamente.
    url = f"{BASE_URI}{EndpointCorreoImportant.GET_CORREO_IMPORTANT.value}"
    headers = get_headers(USERNAME, PASSWORD)
    response = EspoCRMRequest.get_with_url_headers(url, headers)
    assert_status_code_ok(response)

@pytest.mark.smoke
def test_get_email_schema_validation(get_headers):
    # Prueba que verifica si la estructura del JSON de respuesta coincide con el esquema esperado.
    url = f"{BASE_URI}{EndpointCorreoImportant.GET_CORREO_IMPORTANT.value}"
    response = requests.get(url, headers=get_headers(USERNAME, PASSWORD))
    print("\n reponce del Get de correos \n"+str(response.json()))
    assert_schema_correoImportant(response.json())

@pytest.mark.regression
def test_get_email_response_format(get_headers):
    # Prueba que verifica si el formato de la respuesta es 'application/json'.
    url = f"{BASE_URI}{EndpointCorreoImportant.GET_CORREO_IMPORTANT.value}"
    response = requests.get(url, headers=get_headers(USERNAME, PASSWORD))
    assert_content_type_applicationJson(response)

@pytest.mark.regression
def test_get_email_invalid_cookie_in_headers(get_header_cookie):
    # Prueba que verifica si una cookie incorrecta en los encabezados devuelve un estado no autorizado (401).
    url = f"{BASE_URI}{EndpointCorreoImportant.GET_CORREO_IMPORTANT.value}"
    headers = get_header_cookie(USERNAME, PASSWORD)
    headers['Cookie'] = 'wrongCookie'
    response = requests.get(url, headers=headers)
    assert_status_code_unauthorized(response)

@pytest.mark.regression
def test_get_email_invalid_authorization_in_headers(get_header_cookie):
    # Prueba que verifica si una autorización básica incorrecta devuelve un estado no autorizado (401).
    url = f"{BASE_URI}{EndpointCorreoImportant.GET_CORREO_IMPORTANT.value}"
    headers = get_header_cookie(USERNAME, PASSWORD)
    invalidAuth = base64.b64encode(b"invalidUser1232:invalidPassword456").decode('utf-8')
    headers['Authorization'] = 'Basic ' + invalidAuth
    response = requests.get(url, headers=headers)
    assert_status_code_unauthorized(response)

@pytest.mark.regression
def test_get_mail_invalid_order_parameter(get_headers):
    # Prueba que verifica si un parámetro de orden incorrecto devuelve un estado de solicitud incorrecta (400).
    url = f"{BASE_URI}/Email?select=dateSent%2Csubject%2CfromName&maxSize=20&offset=0&orderBy=dateSent&order=invalidOrder"
    response = requests.get(url, headers=get_headers("admin", "admin"))
    assert response.status_code == 400

@pytest.mark.regression
def test_get_mail_valid_maxsize_parameter(get_headers):
    # Prueba que verifica si un parámetro de tamaño máximo válido devuelve un estado exitoso (200).
    url = f"{BASE_URI}/Email?select=dateSent%2Csubject%2CfromName&maxSize=1&offset=0&orderBy=dateSent&order=desc"
    response = requests.get(url, headers=get_headers("admin", "admin"))
    assert_status_code_ok(response)

@pytest.mark.regression
def test_get_mail_missing_auth_token_secret():
    # Prueba que verifica si falta el token de autenticación devuelve un estado no autorizado (401).
    url = f"{BASE_URI}/Email"
    headers = {"Cookie": "some_other_cookie=some_value"}
    response = requests.get(url, headers=headers)
    assert_status_code_unauthorized(response)

@pytest.mark.regression
def test_get_mail_valid_offset_parameter(get_headers):
    # Prueba que verifica si un parámetro de desplazamiento válido devuelve un estado exitoso (200).
    url = f"{BASE_URI}/Email?select=dateSent%2Csubject%2CfromName&maxSize=20&offset=1000&orderBy=dateSent&order=desc"
    response = requests.get(url, headers=get_headers("admin", "admin"))
    assert_status_code_ok(response)

@pytest.mark.regression
def test_get_mail_invalid_basic_authorization():
    # Prueba que verifica si una autorización básica incorrecta devuelve un estado no autorizado (401).
    url = f"{BASE_URI}/Email"
    headers = {"Authorization": "Basic invalidcredentials"}
    response = requests.get(url, headers=headers)
    assert_status_code_unauthorized(response)

@pytest.mark.regression
def test_get_mail_missing_auth_token_secret():
    # Prueba que verifica si falta el token de autenticación devuelve un estado no autorizado (401).
    url = f"{BASE_URI}/Email"
    headers = {"Cookie": "some_other_cookie=some_value"}
    response = requests.get(url, headers=headers)
    assert_status_code_unauthorized(response)
