import json
from jsonschema import validate

def assert_schema_presentation(instance):
    with open("src/resources/schemas/presentation.json", "r") as schema_file:
        schema = json.load(schema_file)
    validate(instance=instance, schema=schema)


def assert_schema_email(instance):
    with open("src/resources/schemas/email.json", "r") as schema_file:
        schema = json.load(schema_file)

def assert_schema_task(instance):
    with open("src/resources/schemas/task.json", "r") as schema_file:
        schema = json.load(schema_file)
    validate(instance=instance, schema=schema)

def assert_schema_calls_without_filters(instance):
    with open("src/resources/schemas/get_completeFields_all_calls_schema.json", "r") as schema_file:
        schema = json.load(schema_file)
    validate(instance=instance, schema=schema)

def assert_schema_correoImportant(instance):
    with open("src/resources/schemas/correoImportant.json", "r") as schema_file:
        schema = json.load(schema_file)
    print("\n schema de correo \n" + str(schema))

    validate(instance=instance, schema=schema)

def assert_schema_calls_without_params(instance):

    with open("src/resources/schemas/get_completeFields_all_calls_schema.json", "r") as schema_file:
        schema = json.load(schema_file)
    validate(instance=instance, schema=schema)


def assert_schema_call_with_specifiedFilters(instance, fieldsToKeep):
    with open("src/resources/schemas/get_completeFields_all_calls_schema.json", "r") as schema_file:
        schema = json.load(schema_file)
        str_fields_to_keep = str(fieldsToKeep)
        fields_to_keep = str_fields_to_keep.split('%2C')
        def filter_properties(properties):
            return {key: value for key, value in properties.items() if key in fields_to_keep}

            # Update the properties of items in the list
        if 'properties' in schema and 'list' in schema['properties']:
            list_items = schema['properties']['list']['items']
            if 'properties' in list_items:
                list_items['properties'] = filter_properties(list_items['properties'])
                if 'required' in list_items:
                    list_items['required'] = [field for field in list_items['required'] if field in fields_to_keep]

    print("\n New schema segun filtros \n"+ str(schema))
    validate(instance=instance, schema=schema)
def assert_schema_activity(instance):
    with open("src/resources/schemas/activity.json", "r") as schema_file:
        schema = json.load(schema_file)

    validate(instance=instance, schema=schema)


