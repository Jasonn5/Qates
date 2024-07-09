email_insert_image_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "type": {"type": "string"},
        "role": {"type": "string"},
        "global": {"type": "boolean"},
        "size": {"type": "integer"},
        "relatedType": {"type": "string"},
        "file": {"type": "string"},
        "field": {"type": "string"}
    },
    "required": [
        "name",
        "type",
        "role",
        "global",
        "size",
        "relatedType",
        "file",
        "field"
    ]
}
