from app.schemas.user import UserResponse
from app.api.dependencies import UserServiceDep
from app.schemas.user import UserCreate
from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/add")
def create_user(
    user: UserCreate,
    service: UserServiceDep,
) -> UserResponse:
    return service.create_user(user)
