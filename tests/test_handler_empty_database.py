import pytest
import os
import sys
import json

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import handler



SOURCE_JSON = "../input/input_213.json"
DEST_JSON = os.getenv("DEST_JSON")


def deleteContent(fName):
    with open(fName, "w"):
        pass


def test_ED_json_with_proper_statusCode():
    response = handler.hello("/")
    assert response["statusCode"] == 200


def test_ED__json_with_proper_messageBody():
    response = handler.hello("/")
    assert str(response["body"]) == '"bruvio welcomes you!"'


def test_ED__json_with_proper_mimetype():
    # let's make sure responses are application/json
    response = handler.hello("/")
    assert response["headers"]["Content-Type"] == "application/json"


@pytest.mark.xfail(reason="empty database")
def test_ED__VinInDatabase():
    # arrange
    SOURCE_JSON = "../input/input_213.json"
    f = open(SOURCE_JSON)
    event = json.load(f)
    f.close()
    # act
    response = handler.getVin(event, context=None)
    expected_response = {
        "vehicle": {
            "CustomerId": 1,
            "VIN": "WDBJF65J1YB039105",
            "Make": None,
            "Model": None,
            "Year": None,
            "ImportedDate": None,
        }
    }
    # assert
    assert response == expected_response


def test_ED__EmptyDatabase():
    # arrange
    SOURCE_JSON = "../input/input_213.json"
    f = open(SOURCE_JSON)
    event = json.load(f)
    f.close()
    # act
    response = handler.getVin(event, context=None)
    expected_response = {
        "statusCode": 404,
        "body": '{"message": "no vehicle with that VIN in database!", "input": {"CustomerId": 213, "VIN": "WDBJF65J1YB039213"}}',
    }
    # assert
    assert response == expected_response


def test_ED__putVin():
    SOURCE_JSON = "../input/input_213.json"
    f = open(SOURCE_JSON)
    event = json.load(f)
    f.close()
    # act
    response = handler.postVin(event, context=None)
    expected_response = {
        "CustomerId": 213,
        "VIN": "WDBJF65J1YB039213",
        "Make": None,
        "Model": None,
        "Year": None,
        "ImportedDate": None,
    }
    deleteContent(DEST_JSON)
    # assert
    assert response == expected_response
