import pytest
import jsonschema
import json
from jsonschema import validate

def assert_itemList_size_is_maxsize(responseJson, maxsize):
    print("\n This is the maxsize sent through params: " + str(maxsize))
    list_size = len(responseJson['list'])
    print("\n This is the size of the list of the response: "+ str(list_size))
    print("\n " + str(responseJson['list']))
    assert list_size==maxsize
def assert_list_acsOrder_with_OrderBy_Order_params(responseJason):
    assert responseJason is not None, "Data should not be None"
    dates = [item['dateEnd'] for item in responseJason['list']]
    assert dates == sorted(dates), "Data should be ordered by dateEnd in ascending order"

