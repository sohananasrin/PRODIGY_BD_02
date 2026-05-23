from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import engine, SessionLocal
from models import Base, User
from schemas import UserCreate, UserResponse

app = FastAPI()

Base.metadata.create_all(bind=engine)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@app.get("/")
def home():

    return {
        "message": "Database connected successfully!"
    }


@app.post("/users", response_model=UserResponse)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    new_user = User(

        name=user.name,
        email=user.email,
        age=user.age

    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return new_user
@app.get(
    "/users",
    response_model=list[UserResponse]
)

def get_users(
    db: Session = Depends(get_db)
):

    users = db.query(User).all()

    return users
@app.put(
    "/users/{user_id}",
    response_model=UserResponse
)

def update_user(
    user_id: str,
    updated_user: UserCreate,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:

         raise HTTPException(
        status_code=404,
        detail="User not found"
    )
    user.name = updated_user.name
    user.email = updated_user.email
    user.age = updated_user.age

    db.commit()

    db.refresh(user)

    return user
@app.delete("/users/{user_id}")

def delete_user(
    user_id: str,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    db.delete(user)

    db.commit()

    return {
        "message": "User deleted successfully"
    }