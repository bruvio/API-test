# Test API

Setting up a REST API [RESTful Web Services](https://en.wikipedia.org/wiki/Representational_state_transfer#Applied_to_web_services) running on AWS Lambda using the traditional Serverless Framework allowing the user to create, list, get, update and delete Vehicle information. DynamoDB is used to store the data.

## Anatomy of the application

The API is to provide VIN (Vehicle Identification Number) storage and decoding functionality.

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

You also need AWS Command Line Interface (cli) installed see [link](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)

Finally you need to install the serverless cli

```bash
# Step 1: Install Node:
# Go to: https://nodejs.org/en/download/package-manager/

# Step 2: Install serverless
npm install -g serverless

# Step 3: Setup serverless
serverless config credentials --provider aws --key <yourkey> --secret <yoursecret> --profile <profilename>
```

### Deployment

This example is made to work with the Serverless Framework dashboard, which includes advanced features such as CI/CD, monitoring, metrics, etc.

In order to deploy with dashboard, you need to first login with:

```bash
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

```bash
Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Injecting required Python packages to package...
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading artifacts...
Serverless: Uploading service dynamodb-api.zip file to S3 (25.3 MB)...
Serverless: Validating template...
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
CloudFormation - UPDATE_IN_PROGRESS - AWS::CloudFormation::Stack - dynamodb-api-dev
CloudFormation - UPDATE_IN_PROGRESS - AWS::Lambda::Function - AllLambdaFunction
CloudFormation - UPDATE_IN_PROGRESS - AWS::Lambda::Function - UpdateLambdaFunction
CloudFormation - UPDATE_IN_PROGRESS - AWS::Lambda::Function - GetLambdaFunction
CloudFormation - UPDATE_IN_PROGRESS - AWS::Lambda::Function - DeleteLambdaFunction
CloudFormation - UPDATE_IN_PROGRESS - AWS::Lambda::Function - CreateLambdaFunction
CloudFormation - UPDATE_COMPLETE - AWS::Lambda::Function - DeleteLambdaFunction
CloudFormation - UPDATE_COMPLETE - AWS::Lambda::Function - AllLambdaFunction
CloudFormation - UPDATE_COMPLETE - AWS::Lambda::Function - GetLambdaFunction
CloudFormation - UPDATE_COMPLETE - AWS::Lambda::Function - CreateLambdaFunction
CloudFormation - UPDATE_COMPLETE - AWS::Lambda::Function - UpdateLambdaFunction
CloudFormation - CREATE_IN_PROGRESS - AWS::Lambda::Version - AllLambdaVersionoAwUWVvyNH4dfavnUN3BJyHQpvblBXyinLKFvTXAQic
CloudFormation - CREATE_IN_PROGRESS - AWS::Lambda::Version - DeleteLambdaVersionJjUIW07EFV2dxvlx9NYTG3dGE4RXQTEHwP1LNJIVpSs
CloudFormation - CREATE_IN_PROGRESS - AWS::Lambda::Version - UpdateLambdaVersion8xUqTWmve4i4oSS8D71PpP0qBsM0S4IsY7t1ApdDlTY
CloudFormation - CREATE_IN_PROGRESS - AWS::Lambda::Version - GetLambdaVersionIsAQuL6Y2JLdEoXIR7SbjT1a7nSTDtX6vjq1IpJc9g
CloudFormation - CREATE_IN_PROGRESS - AWS::Lambda::Version - CreateLambdaVersionfTQNSXglwf56XMI24zPo9muP6cre74qSGkAI91hHiNo
CloudFormation - CREATE_IN_PROGRESS - AWS::Lambda::Version - AllLambdaVersionoAwUWVvyNH4dfavnUN3BJyHQpvblBXyinLKFvTXAQic
CloudFormation - CREATE_COMPLETE - AWS::Lambda::Version - AllLambdaVersionoAwUWVvyNH4dfavnUN3BJyHQpvblBXyinLKFvTXAQic
CloudFormation - CREATE_IN_PROGRESS - AWS::Lambda::Version - DeleteLambdaVersionJjUIW07EFV2dxvlx9NYTG3dGE4RXQTEHwP1LNJIVpSs
CloudFormation - CREATE_IN_PROGRESS - AWS::Lambda::Version - UpdateLambdaVersion8xUqTWmve4i4oSS8D71PpP0qBsM0S4IsY7t1ApdDlTY
CloudFormation - CREATE_COMPLETE - AWS::Lambda::Version - DeleteLambdaVersionJjUIW07EFV2dxvlx9NYTG3dGE4RXQTEHwP1LNJIVpSs
CloudFormation - CREATE_COMPLETE - AWS::Lambda::Version - UpdateLambdaVersion8xUqTWmve4i4oSS8D71PpP0qBsM0S4IsY7t1ApdDlTY
CloudFormation - CREATE_IN_PROGRESS - AWS::Lambda::Version - CreateLambdaVersionfTQNSXglwf56XMI24zPo9muP6cre74qSGkAI91hHiNo
CloudFormation - CREATE_IN_PROGRESS - AWS::Lambda::Version - GetLambdaVersionIsAQuL6Y2JLdEoXIR7SbjT1a7nSTDtX6vjq1IpJc9g
CloudFormation - CREATE_COMPLETE - AWS::Lambda::Version - CreateLambdaVersionfTQNSXglwf56XMI24zPo9muP6cre74qSGkAI91hHiNo
CloudFormation - CREATE_COMPLETE - AWS::Lambda::Version - GetLambdaVersionIsAQuL6Y2JLdEoXIR7SbjT1a7nSTDtX6vjq1IpJc9g
CloudFormation - CREATE_IN_PROGRESS - AWS::ApiGateway::Deployment - ApiGatewayDeployment1619534669808
CloudFormation - CREATE_IN_PROGRESS - AWS::ApiGateway::Deployment - ApiGatewayDeployment1619534669808
CloudFormation - CREATE_COMPLETE - AWS::ApiGateway::Deployment - ApiGatewayDeployment1619534669808
CloudFormation - UPDATE_COMPLETE_CLEANUP_IN_PROGRESS - AWS::CloudFormation::Stack - dynamodb-api-dev
CloudFormation - DELETE_IN_PROGRESS - AWS::ApiGateway::Deployment - ApiGatewayDeployment1619533696977
CloudFormation - DELETE_SKIPPED - AWS::Lambda::Version - GetLambdaVersionYzyG7pCfth3kRiN5c13cpz18T4PRySOwsWIhjCfg
CloudFormation - DELETE_SKIPPED - AWS::Lambda::Version - DeleteLambdaVersion9DZGBnYBke6IiZKOBvtG3SuA881AZotwiodtqDdA
CloudFormation - DELETE_SKIPPED - AWS::Lambda::Version - UpdateLambdaVersiongbVfbtsQKRrpiZnXEiFRclzFd89voHxaqCZcNfVBo
CloudFormation - DELETE_SKIPPED - AWS::Lambda::Version - CreateLambdaVersionlcp2YuPOEigS1UpE3QqqX26c8jyCiSNra2YhdGtlIE
CloudFormation - DELETE_SKIPPED - AWS::Lambda::Version - AllLambdaVersion9NbapzkIdiA3AjIM2bvNj7IOpUdSKtQz6zfJ9R8R6n0
CloudFormation - DELETE_COMPLETE - AWS::ApiGateway::Deployment - ApiGatewayDeployment1619533696977
CloudFormation - UPDATE_COMPLETE - AWS::CloudFormation::Stack - dynamodb-api-dev
Serverless: Stack update finished...
Service Information
service: dynamodb-api
stage: dev
region: us-east-1
stack: dynamodb-api-dev
resources: 40
api keys:
  None
endpoints:
  POST - https://nhcyoo24tl.execute-api.us-east-1.amazonaws.com/dev/VIN/create
  GET - https://nhcyoo24tl.execute-api.us-east-1.amazonaws.com/dev/VIN/get/{VIN}
  GET - https://nhcyoo24tl.execute-api.us-east-1.amazonaws.com/dev/VIN/list
  PUT - https://nhcyoo24tl.execute-api.us-east-1.amazonaws.com/dev/VIN/update/{VIN}
  DELETE - https://nhcyoo24tl.execute-api.us-east-1.amazonaws.com/dev/VIN/delete/{VIN}
functions:
  create: dynamodb-api-dev-create
  get: dynamodb-api-dev-get
  all: dynamodb-api-dev-all
  update: dynamodb-api-dev-update
  delete: dynamodb-api-dev-delete
layers:
  None

Stack Outputs
AllLambdaFunctionQualifiedArn: arn:aws:lambda:us-east-1:546123287190:function:dynamodb-api-dev-all:26
DeleteLambdaFunctionQualifiedArn: arn:aws:lambda:us-east-1:546123287190:function:dynamodb-api-dev-delete:26
CreateLambdaFunctionQualifiedArn: arn:aws:lambda:us-east-1:546123287190:function:dynamodb-api-dev-create:26
GetLambdaFunctionQualifiedArn: arn:aws:lambda:us-east-1:546123287190:function:dynamodb-api-dev-get:26
UpdateLambdaFunctionQualifiedArn: arn:aws:lambda:us-east-1:546123287190:function:dynamodb-api-dev-update:26
ServiceEndpoint: https://nhcyoo24tl.execute-api.us-east-1.amazonaws.com/dev
ServerlessDeploymentBucketName: dynamodb-api-dev-serverlessdeploymentbucket-cx3hu8qyi499

Serverless: Removing old service artifacts from S3...
```

_Note_: In current form, after deployment, your API is public and can be invoked by anyone.

### Testing

tests are implemented using pytest

```bash
pip install -r requirements.txt
cd tests
./tests.sh
```
