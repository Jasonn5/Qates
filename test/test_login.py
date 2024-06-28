import pytest
import responses
from pages.login_page import LoginPage

@pytest.fixture(scope="module")
def login_page(base_url):
    return LoginPage(base_url)

@responses.activate
def test_get_login_success(login_page):
    responses.add(
        responses.GET,
        'https://espo.spartan-soft.com/api/v1/App/user',
        json={"user": "info"},
        status=200
    )

    username = 'admin'
    password = 'admin'
    response = login_page.login(username, password)

    assert response.status_code == 200
    assert response.json() == {"user": "info"}

@responses.activate
def test_get_login_invalid_username(login_page):
    responses.add(
        responses.GET,
        'https://espo.spartan-soft.com/api/v1/App/user',
        json={"error": "Unauthorized"},
        status=401
    )

    username = 'invalid'
    password = 'admin'
    response = login_page.login(username, password)

    assert response.status_code == 401
    assert response.json() == {"error": "Unauthorized"}

@responses.activate
def test_get_login_invalid_password(login_page):
    responses.add(
        responses.GET,
        'https://espo.spartan-soft.com/api/v1/App/user',
        json={"error": "Unauthorized"},
        status=401
    )

    username = 'admin'
    password = 'invalid'
    response = login_page.login(username, password)

    assert response.status_code == 401
    assert response.json() == {"error": "Unauthorized"}

@responses.activate
def test_get_login_invalid_username_and_password(login_page):
    responses.add(
        responses.GET,
        'https://espo.spartan-soft.com/api/v1/App/user',
        json={"error": "Unauthorized"},
        status=401
    )

    username = 'invalid'
    password = 'invalid'
    response = login_page.login(username, password)

    assert response.status_code == 401
    assert response.json() == {"error": "Unauthorized"}

if __name__ == '__main__':
    pytest.main()
