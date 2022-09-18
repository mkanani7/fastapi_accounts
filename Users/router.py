from fastapi import APIRouter
from Users import schemas, crud
from sqlalchemy.orm import Session
from fastapi import Depends
from database import get_db
from fastapi import HTTPException
from typing import List

router = APIRouter(prefix="/user-api/users")

@router.get("/", response_model=List[schemas.UserInfo])
async def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@router.post("/", response_model=schemas.UserInfo)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)
