import json

def assert_content_type_applicationJson(response):
    assert response.headers['Content-Type'] == 'application/json'

def assert_content_type_applicationJson(response):
    assert response.headers["Content-Type"] == "application/json", \
        f"Expected Content-Type to be 'application/json' but got '{response.headers['Content-Type']}'"
