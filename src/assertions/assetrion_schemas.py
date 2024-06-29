import pytest
import jsonschema
import json
from jsonschema import validate

def assert_schema_presentation(instance):
    with open("src/resources/schemas/presentation.json", "r") as schema_file:
        schema = json.load(schema_file)
    validate(instance=instance, schema=schema)