from fastapi.param_functions import Depends
from sqlalchemy.orm import Session
from app.config.database import engine, get_db
from app.schemas.Schema import UserCreate
from app.models.datamodel import User

class UserUpdation:
    def update_user(ID,User_create: UserCreate, db: Session = Depends(get_db)):
        user = db.query(User).filter(User.ID == ID).first()
        user.username = User_create.username
        user.email = User_create.email
        db.commit()
        db.refresh(user)
        return {"message": "User updated successfully", "user": user}