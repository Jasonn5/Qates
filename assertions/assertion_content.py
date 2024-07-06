def assert_empty_array(response):
    response_json = response.json()
    assert isinstance(response_json, list)
    assert len(response_json) == 0, f"Expected empty array but got {len(response_json)} items"

def assert_size_array(response):
    response_json = response.json()
    assert isinstance(response_json, list)
    assert len(response_json) > 0, f"Expected non-empty array but got {len(response_json)} items"
