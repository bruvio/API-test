import json
import logging
import boto3
import datetime
import os
import utility_dynamo

logger = logging.getLogger()
logger.setLevel(logging.INFO)
dynamodb = boto3.client("dynamodb")
print(os.environ["DYNAMODB_TABLE"])
table_name = os.environ["DYNAMODB_TABLE"]


def create(event, context):
    logger.info(f"Incoming request is: {event}")

    # Set the default error response
    response = {"statusCode": 500, "body": "An error occured while creating VIN."}
    VIN_str = event["body"]
    VIN = json.loads(VIN_str)
    current_timestamp = datetime.datetime.now().isoformat()
    VIN["Date"] = current_timestamp

    res = dynamodb.put_item(TableName=table_name, Item=utility_dynamo.to_item(VIN))

    # If creation is successful
    if res["ResponseMetadata"]["HTTPStatusCode"] == 200:
        response = {
            "statusCode": 201,
        }

    return response


def get(event, context):
    logger.info(f"Incoming request is: {event}")
    # Set the default error response
    response = {"statusCode": 500, "body": "An error occured while getting VIN."}
    VIN_id = event["pathParameters"]["VIN"]

    VIN_query = dynamodb.get_item(TableName=table_name, Key={"VIN": {"S": VIN_id}})

    if "Item" in VIN_query:
        VIN = VIN_query["Item"]
        logger.info(f"Vehicle is: {VIN}")
        vehicleDB = utility_dynamo.to_dict(VIN)
        vehicle = dict()
        vehicle["CustomerId"] = vehicleDB.get("CustomerId")
        vehicle["VIN"] = vehicleDB.get("VIN")
        vehicle["Make"] = vehicleDB.get("Make")
        vehicle["Model"] = vehicleDB.get("Model")
        vehicle["Year"] = vehicleDB.get("Year")
        vehicle["Date"] = vehicleDB.get("Date")

        response = {"statusCode": 200, "body": json.dumps(vehicle)}

    return response


def list(event, context):
    # Set the default error response
    response = {"statusCode": 500, "body": "An error occured while getting all VINs."}

    scan_result = dynamodb.scan(TableName=table_name)["Items"]

    VINs = []

    for item in scan_result:
        vehicleDB = utility_dynamo.to_dict(item)
        vehicle = dict()
        vehicle["CustomerId"] = vehicleDB.get("CustomerId")
        vehicle["VIN"] = vehicleDB.get("VIN")
        vehicle["Make"] = vehicleDB.get("Make")
        vehicle["Model"] = vehicleDB.get("Model")
        vehicle["Year"] = vehicleDB.get("Year")
        vehicle["Date"] = vehicleDB.get("Date")
        VINs.append(vehicle)

    response = {"statusCode": 200, "body": json.dumps(VINs)}

    return response


def update(event, context):
    import pdb

    VIN = {"CustomerId": "pippo", "Make": "Fiat"}

    logger.info(f"Incoming request is: {event}")
    #
    VIN_id = event["pathParameters"]["VIN"]
    logger.info(f"Updating {VIN_id}")
    # Set the default error response
    response = {
        "statusCode": 500,
        "body": f"An error occured while updating VIN {VIN_id}",
    }
    VIN_str = event["body"]

    VIN = json.loads(VIN_str)
    vehicle = dict()
    for key in VIN.keys():
        vehicle[key]=VIN.get(key)

    res = dynamodb.update_item(
        TableName=table_name,
        Key={"VIN": {"S": VIN_id}},
        UpdateExpression="set CustomerId=:c, Make=:m, Model=:mo, ModelYear=:my,  updatedON=:u",
        ExpressionAttributeValues={
            ":c": utility_dynamo.to_item(vehicle.get("CustomerId","")),
            ":m": utility_dynamo.to_item(vehicle.get("Make","")),
            ":mo": utility_dynamo.to_item(vehicle.get("Model","")),
            ":my": utility_dynamo.to_item(vehicle.get("ModelYear","")),
            ":u": utility_dynamo.to_item(datetime.datetime.now().isoformat()),
        },
        ReturnValues="UPDATED_NEW",
    )

    # If updation is successful for VIN
    if res["ResponseMetadata"]["HTTPStatusCode"] == 200:
        response = {
            "statusCode": 200,
        }

    return response


def delete(event, context):
    logger.info(f"Incoming request is: {event}")

    VIN_id = event["pathParameters"]["VIN"]
    # Set the default error response
    response = {
        "statusCode": 500,
        "body": f"An error occured while deleting VIN {VIN_id}",
    }

    res = dynamodb.delete_item(TableName=table_name, Key={"VIN": {"S": VIN_id}})

    # If deletion is successful for VIN
    if res["ResponseMetadata"]["HTTPStatusCode"] == 200:
        response = {
            "statusCode": 204,
        }
    return response
