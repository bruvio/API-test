import os
import sys
import logging
import boto3
import utility_dynamo
import requests
import pytest
logger = logging.getLogger()
logger.setLevel(logging.INFO)


dynamodb = boto3.client("dynamodb")
table_name = "dynamodb-api-dev"
os.environ["DYNAMODB_TABLE"] = table_name
api_id = os.getenv("APiID")
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

print(table_name)


def test_Create():

    newHeaders = {"Content-type": "application/json"}
    url = "https://{}.execute-api.us-east-1.amazonaws.com/dev/VIN/create".format(api_id)
    response = requests.post(
        url, json={"CustomerId": 211, "VIN": "WDBJF65J1YB039211"}, headers=newHeaders
    )

    assert response.status_code == 201


def test_List():

    newHeaders = {"Content-type": "application/json"}
    url = "https://{}.execute-api.us-east-1.amazonaws.com/dev/VIN/list".format(api_id)
    response = requests.get(url, headers=newHeaders)

    assert response.status_code == 200


def test_Get():

    newHeaders = {"Content-type": "application/json"}
    url = "https://{}.execute-api.us-east-1.amazonaws.com/dev/VIN/get/WDBJF65J1YB039211".format(
        api_id
    )
    response = requests.get(url, headers=newHeaders)

    assert response.status_code == 200


def test_Update():

    newHeaders = {"Content-type": "application/json"}
    url = "https://{}.execute-api.us-east-1.amazonaws.com/dev/VIN/update/WDBJF65J1YB039211".format(
        api_id
    )
    response = requests.put(
        url,
        json={
            "CustomerId": "bruno",
        },
        headers=newHeaders,
    )

    assert response.status_code == 200

# @pytest.mark.skip(reason='check Dynamodb table')
def test_Delete():

    newHeaders = {"Content-type": "application/json"}
    url = "https://{}.execute-api.us-east-1.amazonaws.com/dev/VIN/delete/WDBJF65J1YB039211".format(
        api_id
    )
    response = requests.delete(url, headers=newHeaders)

    assert response.status_code == 204
