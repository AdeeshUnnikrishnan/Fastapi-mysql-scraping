
from sqlalchemy import Column, Integer, String, VARCHAR
from app.config.database import Base

class User(Base):
    __tablename__ = "users"
    ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(VARCHAR(200), unique=True, index=True)
    email = Column(VARCHAR(200), unique=True, index=True)
