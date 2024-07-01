def assert_scope_meeting(response):
    response_json = response.json()
    assert isinstance(response_json, list)
    for activity in response_json:
        assert activity['scope'] == 'Meeting', f"Expected 'scope' to be 'Meeting' but got '{activity['scope']}'"
def assert_scope_call(response):
    response_json = response.json()
    assert isinstance(response_json, list)
    for activity in response_json:
        assert activity['scope'] == 'Call', f"Expected 'scope' to be 'Call but got '{activity['scope']}'"
def assert_scope_task(response):
    response_json = response.json()
    assert isinstance(response_json, list)
    for activity in response_json:
        assert activity['scope'] == 'Task', f"Expected 'scope' to be 'Task' but got '{activity['scope']}'"
