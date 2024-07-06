def assert_status_code_ok(response):
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

def assert_status_code_created(response):
    assert response.status_code == 201, f"Expected status code 201 but got {response.status_code}"

def assert_status_code_not_found(response):
    assert response.status_code == 404, f"Expected status code 404 but got {response.status_code}"

def assert_status_code_internal_server_error(response):
    assert response.status_code == 500, f"Expected status code 500 but got {response.status_code}"

def assert_status_code_unauthorized(response):
    assert response.status_code == 401, f"Expected status code 401 but got {response.status_code}"

def assert_status_code_forbidden(response):
    assert response.status_code == 403, f"Expected status code 403 but got {response.status_code}"

def assert_status_bad_request(response):
    assert response.status_code == 400, f"Expected status code 400 but got {response.status_code}"

def assert_status_code_method_not_allowed(response):
    assert response.status_code == 405, f"Expected status code 405 but got {response.status_code}"

