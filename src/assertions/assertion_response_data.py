import pytest
import jsonschema
import json
from jsonschema import validate

def assert_itemList_size_is_maxsize(responseJson, maxsize):
    print("\n This is the maxsize sent through params: " + str(maxsize))
    list_size = len(responseJson['list'])
    print("\n This is the size of the list of the response: "+ str(list_size))
    print("\n " + str(responseJson))
    assert list_size==maxsize
def assert_list_acsOrder_with_OrderBy_Order_params(responseJason):
    assert responseJason is not None, "Data should not be None"
    dates = [item['dateEnd'] for item in responseJason['list']]
    assert dates == sorted(dates), "Data should be ordered by dateEnd in ascending order"

def assert_offset_pagination_correctData(response_without_offset, response_with_offset, offset):
    idItemsWithOutOffset = [item['id'] for item in response_without_offset['list']]
    idItemsWithOffset = [item['id'] for item in response_with_offset['list']]

    id_in_positionOffset_idItemsWithOutOffset= idItemsWithOutOffset[offset]
    print("\n This is the id of the call taken from the list of calls with out offset, on the position offset: "+str(id_in_positionOffset_idItemsWithOutOffset))
    firstId_in_idItemsWithOffset = idItemsWithOffset[0]
    print("\n This is the first id of the call taken from the list of calls with offset: "+str(firstId_in_idItemsWithOffset))
    assert id_in_positionOffset_idItemsWithOutOffset == firstId_in_idItemsWithOffset

