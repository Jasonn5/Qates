def assert_delete_success_response_message(response):
    response_text = response.text.strip()
    assert response_text == "true", f"Expected 'true' but got '{response_text}'"

def assert_delete_failed_response_message(response):
    response_text = response.text.strip()
    assert response_text == "", f"Expected 'true' but got '{response_text}'"

