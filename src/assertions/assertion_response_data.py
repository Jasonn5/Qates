import pytest
import jsonschema
import json
from jsonschema import validate

def assert_itemList_size(responseJson, maxsize):
    print("\n This is the maxsize sent through params: " + str(maxsize))
    list_size = len(responseJson['list'])
    print("\n This is the size of the list of the response: "+ str(list_size))
    print("\n " + str(responseJson['list']))
    assert list_size==maxsize
