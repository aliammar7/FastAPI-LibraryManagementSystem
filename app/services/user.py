from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.repositories.user import UserRepository
from app.utils.hashing import hash_password


class UserService:
    def __init__(self) -> None:
        self.repo = UserRepository()

    def create_user(self, db: Session, user_in: UserCreate) -> User:
        user = User(
            email=user_in.email,
            hashed_password=hash_password(user_in.password),
        )
        return self.repo.create(db, user)

    def get_user_by_id(self, db: Session, user_id: int) -> User | None:
        return self.repo.get_by_id(db, user_id)

    def get_user_by_email(self, db: Session, email: str) -> User | None:
        return self.repo.get_by_email(db, email)

    def update_user(
        self,
        db: Session,
        user: User,
        user_in: UserUpdate,
    ) -> User:
        if user_in.email is not None:
            user.email = user_in.email

        if user_in.password is not None:
            user.hashed_password = hash_password(user_in.password)

        return self.repo.update(db, user)

    def delete_user(self, db: Session, user: User) -> None:
        self.repo.delete(db, user)
