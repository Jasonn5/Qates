import json

def assert_content_type_applicationJson(response):
    assert response.headers['Content-Type'] == 'application/json'