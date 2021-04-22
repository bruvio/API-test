import json
from json.decoder import JSONDecodeError
import os

if os.environ.get("DEST_JSON") is not None:

    databasefile = os.getenv("DEST_JSON")
else:
    databasefile = "database.json"


print(databasefile)


def hello(event, context=None):
    """welcome endpoint

    Args:
        event ([type]): [description]
        context ([type], optional): [description]. Defaults to None.

    Returns:
        [type]: [prints welcome message]
    """

    body = "bruvio welcomes you!"
    statusCode = 200
    return {
        "statusCode": statusCode,
        "body": json.dumps(body),
        "headers": {"Content-Type": "application/json"},
    }


def noVinGet(input):
    """helper function to print message

    Args:
        input ([type]): [event]

    Returns:
        [json]: [error message]
    """
    body = {
        "message": "no vehicle with that VIN in database!",
        "input": input,
    }
    response = {"statusCode": 404, "body": json.dumps(body)}

    return response


def noPost(input):
    """helper function to print message

    Args:
        input ([type]): [event]

    Returns:
        [json]: [error message]
    """
    body = {
        "message": "ERROR - no vehicle added to database!",
        "input": input,
    }
    response = {"statusCode": 404, "body": json.dumps(body)}
    return response


def getVin(event, context):
    """function to search in database for a vehicle with VIN specified in input json

    Args:
        event ([json]): [json file containing info on vehicle]
        context ([type]): [description]

    Returns:
        [type]: [description]
    """
    print("Received event: " + json.dumps(event, indent=2))
    message = event
    exists = os.path.isfile(databasefile)
    if message.get("VIN") is None:
            return noVinGet(event)
    if exists:

        with open(databasefile, "r") as f:

            try:
                mock_data = json.load(f)


                if len(mock_data) > 0:
                    for car in mock_data:

                        if car["VIN"] == message["VIN"]:
                            vehicle = dict()
                            vehicle["CustomerId"] = car.get("CustomerId")
                            vehicle["VIN"] = car.get("VIN")
                            vehicle["Make"] = car.get("Make")
                            vehicle["Model"] = car.get("Model")
                            vehicle["Year"] = car.get("Year")
                            vehicle["ImportedDate"] = car.get("ImportedDate")
                            return {"vehicle": vehicle}
                    return noVinGet(event)
                else:
                    return noVinGet(event)
            except JSONDecodeError:
                return noVinGet(event)
        f.close()
    else:

        with open(databasefile, "w") as f:
            pass
        f.close()
        return noVinGet(event)


def postVin(event, context):


    print("Received event: " + json.dumps(event, indent=2))
    message = event
    exists = os.path.isfile(databasefile)

    vehicle = dict()
    vehicle["CustomerId"] = message.get("CustomerId")
    vehicle["VIN"] = message.get("VIN")
    vehicle["Make"] = message.get("Make")
    vehicle["Model"] = message.get("Model")
    vehicle["Year"] = message.get("Year")
    vehicle["ImportedDate"] = message.get("ImportedDate")
    exists = os.path.isfile(databasefile)
    output = []
    output.append(vehicle)
    if vehicle["VIN"] is None:
        return noPost(event)
    if exists:

        try:
            f = open(databasefile, "r")
            current_data = json.load(f)
            f.close()
        except JSONDecodeError:
            f = open(databasefile, "w")
            json.dump(output, f, indent=2)
            f.close()
            return vehicle

        # checking if vehicle identified by input VIN is already in database
        for car in current_data:
            output.append(car)
            if car["VIN"] == message["VIN"]:
                # if so return 404 and do nothing
                return noPost(event)


    # if database does not exist create file and append input json
    else:

        with open(databasefile, "w") as f:
            json.dump(output, f, indent=2)
        f.close()
        return vehicle

    f = open(databasefile, "w")
    json.dump(output, f, indent=2)
    f.close()

    return vehicle
