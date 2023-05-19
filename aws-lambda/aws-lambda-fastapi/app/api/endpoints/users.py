import logging

from typing import Optional
from fastapi import APIRouter, HTTPException
from fastapi import Depends
from sqlmodel import Session
from app.model.userrec import UserRec
from app.api import deps
from pydantic import BaseModel, Field

class User(BaseModel):
	id: Optional[int] = None
	version: Optional[int] = None
	name: str = None

	@staticmethod
	def fromDb(ud: UserRec):
		return User(id = ud.id, version = ud.version, name = ud.name)

	def toDb(self):
		return UserRec(id = self.id, version = self.version, name = self.name)

router = APIRouter()

@router.get("/", response_model = list[User])
def get_users(db: Session = Depends(deps.get_db)) -> list[User]:
	dbUsers = (db.query(UserRec)
		.all()
	)
	users = list(map(User.fromDb, dbUsers))
	logging.info(f"Found users in database: count={len(users)}")
	return users

@router.post("/")
def create_user(user: User, db: Session = Depends(deps.get_db)) -> User:
	if (user.id is not None):
		raise HTTPException(status_code = 400, detail = "User id must not be specified in POST")
	if (user.version is not None):
		raise HTTPException(status_code = 400, detail = "User version must not be specified in POST")
	userRec = user.toDb()
	db.add(userRec)
	db.commit()
	logging.info(f"Created user: {userRec}")
	return User.fromDb(userRec)

@router.get("/{id}", response_model = None)
def get_user(id: int, db: Session = Depends(deps.get_db)) -> User:
	userRec = (db.query(UserRec)
		.filter_by(id = id)
		.first()
	)
	if (userRec is None):
		raise HTTPException(status_code = 404, detail = "Item not found")
	return User.fromDb(userRec)

@router.put("/{id}")
def update_user(id: int, user: User, db: Session = Depends(deps.get_db)) -> User:
	userRec = db.query(UserRec).filter_by(id = id).first()
	if (userRec is None):
		raise HTTPException(status_code = 404, detail = "Item not found")
	if (userRec.version != user.version):
		raise HTTPException(status_code = 400, detail = "Versions in input and storage do not match")

	userRec.name = user.name

	db.commit()
	logging.info(f"Updated user: {userRec}")

	return User.fromDb(userRec)

@router.delete("/{id}")
def delete_user(id: int, db: Session = Depends(deps.get_db)) -> dict:
	count = (db.query(UserRec)
		.filter_by(id = id)
		.delete()
	)
	db.commit()

	if (count == 0):
		raise HTTPException(status_code = 404, detail = "Item not found")
	logging.info(f"Deleted user: {id}")

	return { "message": "Deleted user: " + str(id) }

