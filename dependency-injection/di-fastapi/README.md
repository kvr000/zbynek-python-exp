# Dependency Injection FastAPI experiment


## System

```
sudo apt install python3-fastapi uvicorn
```


## Initialization

```
virtualenv -p python3.11 env
source ./env/bin/activate
npx sls plugin install -n serverless-vpc-plugin
serverless plugin install -n serverless-dependson-plugin
pip install -r requirements.txt
```


## Local Run

```
./env/bin/uvicorn app.main:app --reload
```


## Manual Tests

```
export HOST=http://localhost:8080/dev

curl -i -X GET $HOST/

curl -i -X GET $HOST/db/
```
