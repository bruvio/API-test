 #!/bin/bash

export APiID=$(aws apigateway get-rest-apis --query 'items[?contains(name, `dynamodb`) == `true`].id' --output text)
echo "ApiId :" $APiID



python -m pytest -v test_handler.py
