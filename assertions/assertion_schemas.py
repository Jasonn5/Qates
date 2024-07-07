import json
from jsonschema import validate


def assert_schema_presentation(instance):
    with open("resources/schemas/presentation.json", "r") as schema_file:
        schema = json.load(schema_file)
    validate(instance=instance, schema=schema)


def assert_schema_email(instance):
    with open("resources/schemas/email.json", "r") as schema_file:
        schema = json.load(schema_file)
    validate(instance=instance, schema=schema)


def assert_schema_task(instance):
    with open("resources/schemas/task.json", "r") as schema_file:
        schema = json.load(schema_file)
    validate(instance=instance, schema=schema)


def assert_schema_calls_without_filters(instance):
    with open("resources/schemas/get_completeFields_all_calls_schema.json", "r") as schema_file:
        schema = json.load(schema_file)
    validate(instance=instance, schema=schema)


def assert_schema_correoImportant(instance):
    with open("resources/schemas/mail_important.json", "r") as schema_file:
        schema = json.load(schema_file)
    validate(instance=instance, schema=schema)


def assert_schema_call_with_specifiedFilters(instance, fieldsToKeep):
    with open("resources/schemas/get_completeFields_all_calls_schema.json", "r") as schema_file:
        schema = json.load(schema_file)
        fields_to_keep = fieldsToKeep.split('%2C')

        def filter_properties(properties):
            return {key: value for key, value in properties.items() if key in fields_to_keep}

        if 'properties' in schema and 'list' in schema['properties']:
            list_items = schema['properties']['list']['items']
            if 'properties' in list_items:
                list_items['properties'] = filter_properties(list_items['properties'])
                if 'required' in list_items:
                    list_items['required'] = [field for field in list_items['required'] if field in fields_to_keep]
    validate(instance=instance, schema=schema)


def assert_schema_activity(instance):
    with open("resources/schemas/activity.json", "r") as schema_file:
        schema = json.load(schema_file)
    validate(instance=instance, schema=schema)


def assert_schema_contact_post(instance):
    with open("resources/schemas/contact_post.json", "r") as schema_file:
        schema = json.load(schema_file)
    validate(instance=instance, schema=schema)


def assert_schema_error_contact_post(instance):
    with open("resources/schemas/contact_error_post.json", "r") as schema_file:
        schema = json.load(schema_file)
    validate(instance=instance, schema=schema)
