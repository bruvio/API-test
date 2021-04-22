# Test API

test api deployed using Python Flask API service running on AWS Lambda using the traditional Serverless Framework.

## Anatomy of the application

The API to provide VIN (Vehicle Identification Number) storage and decoding functionality.

## Aim

Using AWS serverless technologies, build a small API to provide VIN (Vehicle Identification Number) storage and decoding functionality.

## Requirements

A consumer of the API should be able to:

- import a vehicle by providing a VIN
- get information about a previously-imported vehicle by providing a VIN

Ensure that the json file (in the `/input` folder) can be provided to the API as an input.

Ensure that the output from the API matches the format in the output.example file in the `/output` folder.

## Usage

### Prerequisites

In order to package your dependencies locally with `serverless-python-requirements`, you need to have `Python3.8` installed locally. You can create and activate a dedicated virtual environment with the following command:

```bash
python3.8 -m venv ./venv
source ./venv/bin/activate
```

Alternatively, you can also use `dockerizePip` configuration from `serverless-python-requirements`. For details on that, please refer to corresponding [GitHub repository](https://github.com/UnitedIncome/serverless-python-requirements).

### Deployment

This example is made to work with the Serverless Framework dashboard, which includes advanced features such as CI/CD, monitoring, metrics, etc.

In order to deploy with dashboard, you need to first login with:

```
serverless login
```

install dependencies with:

```
npm install
```

and then perform deployment with:

```
serverless deploy
```

After running deploy, you should see output similar to:

````bash
Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Creating Stack...
Serverless: Checking Stack create progress...
........
Serverless: Stack create finished...
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading artifacts...
Serverless: Uploading service aws-python-rest-api.zip file to S3 (711.23 KB)...
Serverless: Validating template...
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
.................................
Serverless: Stack update finished...
Service Information
service: aws-python-rest-api
stage: dev
region: us-east-1
stack: aws-python-rest-api-dev
resources: 12
api keys:
  None
endpoints:
  ANY - https://xxxxxxx.execute-api.us-east-1.amazonaws.com/dev/
functions:
  api: aws-python-rest-api-dev-hello
layers:
  None

_Note_: In current form, after deployment, your API is public and can be invoked by anyone.

### Invocation

to test the api locally

```bash
serverless invoke local --function postVin --path input/input_213.json
````

Should result in the following response:

```bash
{
    "statusCode": 404,
    "body": "{\"message\": \"ERROR - no vehicle added to database!\", \"input\": {\"CustomerId\": 212, \"VIN\": \"WDBJF65J1YB039212\"}}"
}
```

or

```bash
serverless invoke local --function postVin --path input/input_212.json
```

```bash
{
    "CustomerId": 213,
    "VIN": "WDBJF65J1YB039213",
    "Make": null,
    "Model": null,
    "Year": null,
    "ImportedDate": null
}
```

depending if the vin is in the database or not

to search for a vim

```bash
serverless invoke local --function getVin --path input/input_213.json
```

should result in

```bash
{
    "vehicle": {
        "CustomerId": 213,
        "VIN": "WDBJF65J1YB039213",
        "Make": null,
        "Model": null,
        "Year": null,
        "ImportedDate": null
    }
}
```

if the item is in the database

or

```bash
serverless invoke local --function getVin --path input/input_212.json
database.json
```

```bash
{
    "statusCode": 404,
    "body": "{\"message\": \"no vehicle with that VIN in database!\", \"input\": {\"CustomerId\": 212, \"VIN\": \"WDBJF65J1YB039212\"}}"
}
```

if the item is not in the database.

### Testing

tests are implemented using pytest

```bash
cd tests
./tests.sh
```
