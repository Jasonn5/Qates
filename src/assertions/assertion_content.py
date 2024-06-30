def assert_content_type_json(response):
    assert response.headers['Content-Type'] == 'application/json'
