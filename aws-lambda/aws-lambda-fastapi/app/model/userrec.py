from sqlalchemy import Integer, String, Column, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class UserRec(Base):
    __tablename__ = "UserRec"

    id = Column(Integer, primary_key = True, index = True)
    version = Column(Integer, nullable = False)
    name = Column(String(255), nullable = False)

    __mapper_args__ = { "version_id_col": version }
