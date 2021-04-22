import pytest
import os
import sys
import json

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import handler

SOURCE_JSON = "../input/input_212.json"
DEST_JSON = os.getenv("DEST_JSON")


def test_json_with_proper_statusCode():
    response = handler.hello("/")
    assert response["statusCode"] == 200


def test_json_with_proper_messageBody():
    response = handler.hello("/")
    assert str(response["body"]) == '"bruvio welcomes you!"'


def test_json_with_proper_mimetype():
    # let's make sure responses are application/json
    response = handler.hello("/")
    assert response["headers"]["Content-Type"] == "application/json"


def test_VinInDatabase():
    # arrange
    SOURCE_JSON = "../input/input_212.json"
    f = open(SOURCE_JSON)
    event = json.load(f)
    f.close()
    # act
    print(event)
    resopnse = handler.getVin(event, context=None)
    expected_response = {
        "vehicle": {
            "CustomerId": 212,
            "VIN": "WDBJF65J1YB039212",
            "Make": None,
            "Model": None,
            "Year": None,
            "ImportedDate": None,
        }
    }
    # assert
    assert resopnse == expected_response


# @pytest.mark.skip()
def test_putDuplicateVin():
    # arrange
    SOURCE_JSON = "../input/input_212.json"
    f = open(SOURCE_JSON)
    event = json.load(f)
    f.close()
    # act
    response = handler.postVin(event, context=None)
    expected_response = {
        "statusCode": 404,
        "body": '{"message": "ERROR - no vehicle added to database!", "input": {"CustomerId": 212, "VIN": "WDBJF65J1YB039212"}}',
    }
    # assert
    assert response == expected_response
