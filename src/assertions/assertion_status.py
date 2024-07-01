import pytest

def assert_status_code_ok(response):
    assert response.status_code == 200

def assert_status_code_created(response):
    assert response.status_code == 201

def assert_status_code_not_found(response):
    assert response.status_code == 404

def assert_status_code_internal_server_error(response):
    assert response.status_code == 500

def assert_status_code_unauthorized(response):
    assert response.status_code == 401

def assert_status_code_forbidden(response):
    assert response.status_code == 403

def assert_status_bad_request(response):
    assert response.status_code == 400

