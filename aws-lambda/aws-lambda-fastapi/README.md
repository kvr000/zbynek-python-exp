# AWS Lambda FastAPI experiment

Mix of learnings for Python on AWS Lambda, serverless deployment and cloudformation configuration.


## System

```
sudo apt install python3-fastapi uvicorn
```


## Installation

```
virtualenv -p python3 env
pip install fastapi mangum uvicorn

source ./env/bin/activate
```


## Run

```
./env/bin/uvicorn main:app --reload
```
