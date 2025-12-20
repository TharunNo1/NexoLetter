from app.schemas.user import UserResponse
from sqlalchemy.orm.session import Session
from app.schemas.user import UserCreate
from app.models.user import User

class UserService:

    def __init__(self, db: Session):
        self.db = db 

    def create_user(self, user: UserCreate) -> UserResponse:
        db_user = User(email = user.email)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user