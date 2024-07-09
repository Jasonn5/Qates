def assert_status_code_ok(response):
    assert response.status_code == 200

def assert_status_code_unauthorized(response):
    assert response.status_code == 401

def assert_status_code_bad_request(response):
    assert response.status_code == 400

def assert_status_code_forbidden(response):
    assert response.status_code == 403

def assert_status_code_gateway_timeout(response):
    assert response.status_code == 504

def assert_status_code_service_unavailable(response):
    assert response.status_code == 503

