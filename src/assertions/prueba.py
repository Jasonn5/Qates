import pytest

def assert_status_code(response, status_code):
    assert response.status_code == status_code

