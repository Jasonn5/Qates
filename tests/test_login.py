import requests
import base64
import responses
import pytest
from login import login

BASE_URL = 'https://espo.spartan-soft.com/api/v1'
API_ENDPOINT = '/App/user'

def get_mock_response(status_code, json_data):
    responses.add(
        responses.GET,
        f"{BASE_URL}{API_ENDPOINT}",
        json=json_data,
        status=status_code
    )

@responses.activate
def test_login_success():
    get_mock_response(200, {"user": "info"})
    username = 'admin'
    password = 'admin'
    response = login(username, password)