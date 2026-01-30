from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.user import UserCreate, UserRead
from app.services.user import UserService
from app.api.deps import get_current_user
from app.models.user import User

router = APIRouter(prefix="/users")


@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user(
    user_in: UserCreate,
    db: Session = Depends(get_db),
):
    service = UserService()

    existing = service.get_user_by_email(db, user_in.email)
    if existing:
        raise HTTPException(
            status_code=400,
            detail="Email already registered",
        )

    return service.create_user(db, user_in)


@router.get("/me", response_model=UserRead)
def read_current_user(
    current_user: User = Depends(get_current_user),
):
    return current_user
