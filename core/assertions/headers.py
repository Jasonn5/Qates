def assert_content_type_application_json(response):
    assert response.headers['Content-Type'] == 'application/json', \
        f"Expected Content-Type to be 'application/json' but got '{response.headers['Content-Type']}'"
