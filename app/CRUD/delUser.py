from fastapi.param_functions import Depends
from sqlalchemy.orm import Session
from app.config.database import engine, get_db
from app.schemas.Schema import UserCreate
from app.models.datamodel import User

class UserDeletion:
    def delete_user(user_id: int, db: Session = Depends(get_db)):
        user = db.query(User).filter(User.ID == user_id).first()
        db.delete(user)
        db.commit()