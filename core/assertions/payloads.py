import json
from jsonschema import validate

def assert_payload_calls(instance):
    with open("core/payloads/calls/payload_call_schema.json", "r") as schema_file:
        schema = json.load(schema_file)
    validate(instance=instance, schema=schema)

