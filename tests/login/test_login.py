import requests
import pytest
from src.assertions.prueba import assert_status_code
from config import BASE_URI


def test_get_login_success(get_headers):
    response = requests.get(f'{BASE_URI}/App/user', headers=get_headers("jeyson", "Testing.123!"))
    print(response)
    assert_status_code(response, 200)

def test_get_login_invalid_username(get_headers):
    response = requests.get(f'{BASE_URI}/App/user', headers=get_headers("invalid_user", "Testing.123!"))
    assert_status_code(response, 401)


def test_get_login_invalid_password(get_headers):
    response = requests.get(f'{BASE_URI}/App/user', headers=get_headers("jeyson", "invalid_password"))
    assert_status_code(response, 401)


def test_get_login_invalid_username_and_password(get_headers):
    response = requests.get(f'{BASE_URI}/App/user', headers=get_headers("invalid_user", "invalid_password"))
    assert_status_code(response, 401)

def test_login_empty_fields(get_headers):
    response = requests.get(f'{BASE_URI}/App/user', headers=get_headers("", ""))
    assert_status_code(response, 401)


def test_login_empty_user(get_headers):
    response = requests.get(f'{BASE_URI}/App/user', headers=get_headers("", "Testing.123!"))
    assert_status_code(response, 401)


def test_login_empty_password(get_headers):
    response = requests.get(f'{BASE_URI}/App/user', headers=get_headers("jeyson", ""))
    assert_status_code(response, 401)


