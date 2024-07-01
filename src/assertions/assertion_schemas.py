import json
from jsonschema import validate

def assert_schema_presentation(instance):
    with open("src/resources/schemas/presentation.json", "r") as schema_file:
        schema = json.load(schema_file)
    validate(instance=instance, schema=schema)

def assert_schema_task(instance):
    with open("src/resources/schemas/task.json", "r") as schema_file:
        schema = json.load(schema_file)

def assert_schema_correoImportant(instance):
    with open("src/resources/schemas/correoImportant.json", "r") as schema_file:
        schema = json.load(schema_file)
    print("\n schema de correo \n" + str(schema))
    validate(instance=instance, schema=schema)

def assert_schema_calls_without_params(instance):
    with open("src/resources/schemas/get_completeFields_all_calls_schema.json", "r") as schema_file:
        schema = json.load(schema_file)
    validate(instance=instance, schema=schema)

def assert_schema_activity(instance):
    with open("src/resources/schemas/activity.json", "r") as schema_file:
        schema = json.load(schema_file)
    validate(instance=instance, schema=schema)

