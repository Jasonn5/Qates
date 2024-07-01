def assert_empty_array(response):
    response_json = response.json()
    assert isinstance(response_json, list)
    assert len(response_json) == 0


def assert_size_array(response):
    response_json = response.json()
    assert isinstance(response_json, list)
    print(f"Size of array: {len(response_json)}")
    assert len(response_json) > 0
