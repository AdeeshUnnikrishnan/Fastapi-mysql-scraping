from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.param_functions import Depends
from sqlalchemy.orm import Session
from app.config.database import *
from app.config.database import engine, get_db
from app.CRUD.addUser import UserCreation
from app.CRUD.getUser import UserGet
from app.CRUD.delUser import UserDeletion
from app.CRUD.updateUser import UserUpdation
from app.CRUD.scraper import main
from app.models.datamodel import User
from app.schemas.Schema import UserCreate
app = FastAPI()


@app.post("/create-user")
async def create_user_endpoint(User_create:UserCreate, db: Session = Depends(get_db)):
    new_user = UserCreation.create_user(User_create,db)
    return {"message":"user added successfully",
    "User":new_user}

@app.get("/get-all-users")
async def get_all_user(db: Session = Depends(get_db)):
    get_user = UserGet.get_all_users(db)
    return {"User":get_user}

@app.get("/get-user/{id}")
async def get_user_endpoint(id, db: Session = Depends(get_db)):
    get_user = UserGet.get_user(id,db)
    return {"User":get_user}
@app.delete("/delete-user/{id}")
async def delete_user_endpoint(id, db: Session = Depends(get_db)):
    delete_user = UserDeletion.delete_user(id,db)
    return "User deleted"

@app.put("/update-user/{id}")
async def update_user_endpoint(id,User_create:UserCreate, db: Session = Depends(get_db)):
    update_user = UserUpdation.update_user(id,User_create,db)
    return {"User":update_user}

@app.post("/scraping")
async def scrapper():
    scraping = main()
    return {"message":" Data scrapped successfully"}

