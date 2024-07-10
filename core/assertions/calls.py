def assert_delete_success_response_message(response):
    response_text = response.text.strip()
    assert response_text == "true", f"Expected 'true' but got '{response_text}'"

def assert_delete_failed_response_message(response):
    response_text = response.text.strip()
    assert response_text == "", f"Expected 'true' but got '{response_text}'"

def assert_created_success_response_deleted_field(response):
    response_data = response.json()
    value_delete_field = response_data['deleted']
    print("delete field when call created: " + str(value_delete_field))
    assert value_delete_field is False, f"Expected 'False' but got '{value_delete_field}'"

def assert_deleted_success_response_deleted_field(response):
    response_data = response.json()
    value_delete_field = response_data['deleted']
    print("delete field when call deleted: " + str(value_delete_field))
    assert value_delete_field is True, f"Expected 'true' but got '{value_delete_field}'"

