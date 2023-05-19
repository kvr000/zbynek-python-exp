# AWS Lambda Python Rest experiment

Based on tutorial https://www.sicara.fr/blog-technique/2018-05-25-build-serverless-rest-api-15-minutes-aws


## Installation

```
sudo npm install -g serverless

virtualenv venv --python=python3.10
source venv/bin/activate
```

## Initialization

```
serverless create --template aws-python3 --name aws-lambda-rest
serverless plugin install -n serverless-python-requirements
```
