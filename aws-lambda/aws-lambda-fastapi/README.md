# AWS Lambda FastAPI experiment

Mix of learnings for Python on AWS Lambda with RDS database, serverless deployment and cloudformation configuration.


## System

```
sudo apt install python3-fastapi uvicorn
```


## Initialization

```
virtualenv -p python3 env
source ./env/bin/activate
npx sls plugin install -n serverless-vpc-plugin
serverless plugin install -n serverless-dependson-plugin
pip install `cat requirements.txt`

```


## Local Run

```
./env/bin/uvicorn main:app --reload
```


## Manual Tests

```
export HOST=http://localhost:8080/dev

curl -i -X POST -H "Content-Type: application/json" -d '{"name":"Zbynek"}' $HOST/api/users/

curl -i -X GET $HOST/api/users/

curl -i -X GET $HOST/api/users/1

curl -i -X PUT -H "content-type: application/json" -d '{"name":"Vyskovsky"}' $HOST/api/users/1

curl -i -X DELETE $HOST/api/users/1
```
