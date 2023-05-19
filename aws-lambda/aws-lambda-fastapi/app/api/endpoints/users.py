from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_users():
    return {"message": "Users!"}

@router.post("/")
async def create_user():
    return {"message": "Created user!"}

@router.get("/{id}")
async def get_user(id: int):
    return {"message": "This user: " + str(id)}

@router.put("/{id}")
async def update_user(id: int):
    return {"message": "Updated user: " + str(id)}

@router.delete("/{id}")
async def delete_user(id: int):
    return {"message": "Deleted user: " + str(id)}
