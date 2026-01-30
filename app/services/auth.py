from datetime import timedelta
from sqlalchemy.orm import Session

from app.core.security import create_access_token
from app.core.config import settings
from app.repositories.user import UserRepository
from app.utils.hashing import verify_password


class AuthService:
    def __init__(self) -> None:
        self.repo = UserRepository()

    def authenticate_user(
        self,
        db: Session,
        email: str,
        password: str,
    ):
        user = self.repo.get_by_email(db, email)
        if not user:
            return None

        if not verify_password(password, user.hashed_password):
            return None

        return user

    def create_token(self, user_id: int) -> str:
        expires = timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
        return create_access_token(
            subject=user_id,
            expires_delta=expires,
        )
