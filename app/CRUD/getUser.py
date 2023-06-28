from fastapi.param_functions import Depends
from sqlalchemy.orm import Session
from app.config.database import engine, get_db
from app.schemas.Schema import UserCreate
from app.models.datamodel import User

class UserGet:
    def get_user(user_id: int, db: Session = Depends(get_db)):
        user = db.query(User).filter(User.ID == user_id).first()
        return user

    def get_all_users(db: Session = Depends(get_db)):
        users = db.query(User).all()
        return users
