import pytest
import allure
from core.config.config import BASE_URI
from core.assertions.schemas import assert_schema_correoImportant
from core.assertions.headers import assert_content_type_application_json
from core.assertions.status import assert_status_code_ok, assert_status_code_unauthorized
from api.request.api_request import EspoCRMRequest
from api.endpoints.mail_important import EndpointCorreoImportant
from resources.auth.auth import Auth



@allure.suite('EspoCRM')
@allure.sub_suite('Ericka')
@allure.feature('Get email important')
@allure.story('Get email important')
@allure.tag('author: Ericka')
@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_get_email_success(get_headers):
    """
    1. Verificar que obtenga todos los mensajes marcados como Importantes - Status code 200 OK
    """
    url = f"{BASE_URI}{EndpointCorreoImportant.GET_MAIL_IMPORTANT.value}"
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.get_with_url_headers(url, headers)
    assert_status_code_ok(response)

@allure.suite('EspoCRM')
@allure.sub_suite('Ericka')
@allure.feature('Get email important')
@allure.story('Get email important')
@allure.tag('author: Ericka')
@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_get_email_schema_validation(get_headers):
    """
    2. Verificar que el parámetro 'select' contenga algunos campos válidos - Status code 200 OK
    """
    url = f"{BASE_URI}{EndpointCorreoImportant.GET_MAIL_IMPORTANT.value}"
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.get_with_url_headers(url, headers)
    print("\n reponce del Get de correos \n" + str(response.json()))
    assert_schema_correoImportant(response.json())

@allure.suite('EspoCRM')
@allure.sub_suite('Ericka')
@allure.feature('Get email important')
@allure.story('Get email important')
@allure.tag('author: Ericka')
@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_get_email_response_format(get_headers):
    """
    3. Verificar que el formato de la respuesta sea 'application/json'
    """
    url = f"{BASE_URI}{EndpointCorreoImportant.GET_MAIL_IMPORTANT.value}"
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.get_with_url_headers(url, headers)
    assert_content_type_application_json(response)

@allure.suite('EspoCRM')
@allure.sub_suite('Ericka')
@allure.feature('Get email important')
@allure.story('Get email important')
@allure.tag('author: Ericka')
@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_get_email_invalid_authorization_in_headers(get_headers):
    """
    4. Verificar que el header tenga una BasicAuthorization errónea - Status code 401 Unauthorized
    """
    url = f"{BASE_URI}{EndpointCorreoImportant.GET_MAIL_IMPORTANT.value}"
    headers = Auth().auth_invalid_credentials(get_headers)
    response = EspoCRMRequest.get_with_url_headers(url, headers)
    assert_status_code_unauthorized(response)

@allure.suite('EspoCRM')
@allure.sub_suite('Ericka')
@allure.feature('Get email important')
@allure.story('Get email important')
@allure.tag('author: Ericka')
@pytest.mark.functional
@pytest.mark.regression
def test_get_email_invalid_cookie_in_headers(get_header_cookie):
    """
    5. Verificar que el header tenga una cookie sin auth-token-secret - Status code 401 Unauthorized
    """
    url = f"{BASE_URI}{EndpointCorreoImportant.GET_MAIL_IMPORTANT.value}"
    headers = Auth().auth_valid_credential(get_header_cookie)
    headers['Cookie'] = 'wrongCookie'
    response = EspoCRMRequest.get_with_url_headers(url, headers)
    assert_status_code_unauthorized(response)

@allure.suite('EspoCRM')
@allure.sub_suite('Ericka')
@allure.feature('Get email important')
@allure.story('Get email important')
@allure.tag('author: Ericka')
@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_get_mail_valid_offset_parameter(get_header_cookie):
    """
    6. Verificar que el parámetro 'offset' tenga un valor máximo válido - Status code 200 OK
    """
    url = f"{BASE_URI}{EndpointCorreoImportant.GET_MAIL_OFFSET_1000.value}"
    headers = Auth().auth_valid_credential(get_header_cookie)
    response = EspoCRMRequest.get_with_url_headers(url, headers)
    assert_status_code_ok(response)

@allure.suite('EspoCRM')
@allure.sub_suite('Ericka')
@allure.feature('Get email important')
@allure.story('Get email important')
@allure.tag('author: Ericka')
@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_get_mail_valid_maxsize_parameter(get_headers):
    """
    7. Verificar que el parámetro 'maxsize' tenga un valor mínimo válido - Status code 200 OK
    """
    url = f"{BASE_URI}{EndpointCorreoImportant.GET_MAIL_MAXSIZE_1.value}"
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.get_with_url_headers(url, headers)
    assert_status_code_ok(response)

@allure.suite('EspoCRM')
@allure.sub_suite('Ericka')
@allure.feature('Get email important')
@allure.story('Get email important')
@allure.tag('author: Ericka')
@pytest.mark.functional
@pytest.mark.regression
def test_get_mail_invalid_order_parameter(get_headers):
    """
    8. Verificar que el parámetro 'order' contenga valores numéricos/booleanos/strings - Status code 400 Bad Request
    """
    url = f"{BASE_URI}{EndpointCorreoImportant.GET_MAIL_INVALID_ORDER.value}"
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.get_with_url_headers(url, headers)
    assert response.status_code == 400

@allure.suite('EspoCRM')
@allure.sub_suite('Ericka')
@allure.feature('Get email important')
@allure.story('Get email important')
@allure.tag('author: Ericka')
@pytest.mark.functional
@pytest.mark.regression
def test_get_mail_missing_auth_token_secret():
    """
    9. Verificar que el header tenga una cookie sin auth-token-secret - Status code 401 Unauthorized
    """
    url = f"{BASE_URI}/Email"
    headers = {"Cookie": "some_other_cookie=some_value"}
    response = EspoCRMRequest.get_with_url_headers(url, headers)
    assert_status_code_unauthorized(response)

@allure.suite('EspoCRM')
@allure.sub_suite('Ericka')
@allure.feature('Get email important')
@allure.story('Get email important')
@allure.tag('author: Ericka')
@pytest.mark.regression
def test_get_mail_invalid_basic_authorization(get_header_cookie):
    """
    10. Verificar que el header tenga una cookie sin auth-token-secret - Status code 401 Unauthorized
    """
    url = f"{BASE_URI}/Email"
    headers = {"Authorization": "Basic invalidcredentials"}
    response = EspoCRMRequest.get_with_url_headers(url, headers)
    assert_status_code_unauthorized(response)