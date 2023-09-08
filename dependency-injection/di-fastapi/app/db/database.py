import logging

class Database:
    db_name: str = None

    def __init__(self, db_name: str):
        self.db_name = db_name

    def getConnection(self) -> str:
        logging.info(f"Connecting to db: db_name={self.db_name}")
