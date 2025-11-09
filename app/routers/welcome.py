from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models import User
from app.database import get_db
from app.schemas import UserCreate, UserResponse
from typing import List

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

# ✅ Create User
@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if email already exists
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    db_user = User(name=user.name, age=user.age, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# ✅ Read All Users
@router.get("/", response_model=List[UserResponse])
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


# ✅ Get Single User
@router.get("/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found!")
    return db_user


# ✅ Update User
@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found!")

    db_user.name = user.name
    db_user.age = user.age
    db_user.email = user.email
    db.commit()
    db.refresh(db_user)
    return db_user


# ✅ Delete User
@router.delete("/{user_id}", status_code=status.HTTP_200_OK)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found!")

    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}
