email_insert_image_payload = {
    "emailId": "validEmailId",
    "imageData": "base64ImageData"
}

invalid_email_id_payload = {
    "emailId": "invalidEmailId",
    "imageData": "base64ImageData"
}

large_image_payload = {
    "emailId": "validEmailId",
    "imageData": "largeBase64ImageData"
}

empty_body_payload = {}