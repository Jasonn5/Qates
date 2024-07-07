import json
from jsonschema import validate

def assert_payload_calls(instance):
    with open("payloads/calls/payload_call.json", "r") as schema_file:
        schema = json.load(schema_file)
    validate(instance=instance, schema=schema)
