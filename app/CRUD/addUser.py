from fastapi.param_functions import Depends
from sqlalchemy.orm import Session
from app.config.database import engine, get_db
from app.schemas.Schema import UserCreate
from app.models.datamodel import User

class UserCreation:
    def create_user(User_create: UserCreate, db: Session = Depends(get_db)):
        user = User(username=User_create.username, email=User_create.email)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user