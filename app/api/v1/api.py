from fastapi.routing import APIRouter
from .endpoints import users_router

api_router = APIRouter()
api_router.include_router(users_router)