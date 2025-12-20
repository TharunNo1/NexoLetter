from typing import Annotated
from fastapi import Depends
from app.services.user_service import UserService
from app.core.database import SessionLocal

def get_db():
    with SessionLocal() as db:
        yield db 

def get_user_service(db = Depends(get_db)):
    return UserService(db)


UserServiceDep = Annotated[UserService, Depends(get_user_service)]