import os
import boto3
import psycopg2

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from app.model.userrec import UserRec


ENDPOINT = os.environ["FASTAPIEXP_DB_HOST"]
PORT = os.environ["FASTAPIEXP_DB_PORT"]
USER = os.environ["FASTAPIEXP_DB_USER"]
PASS = os.environ["FASTAPIEXP_DB_PASS"]
DBNAME = os.environ["FASTAPIEXP_DB_NAME"]
REGION = os.environ["AWS_REGION"]

auth_token = PASS

#rds_boto3 = boto3.client('rds')
#auth_token = rds_boto3.generate_db_auth_token(
#    DBHostname = ENDPOINT,
#    Port = PORT,
#    DBUsername = USER,
#    Region = REGION
#)

#session = boto3.session.Session()
#client = session.client(
#		service_name = 'secretsmanager',
#		region_name = REGION
#)
#token = client.get_secret_value(SecretId = SECRET_NAME)['SecretString']

engine = create_engine(
		"postgresql+psycopg2://" + USER + ":" + auth_token + "@" + ENDPOINT + ":" + PORT + "/" + DBNAME,
		connect_args = { 'connect_timeout': 4 }
)


UserRec.metadata.create_all(engine)


SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)
