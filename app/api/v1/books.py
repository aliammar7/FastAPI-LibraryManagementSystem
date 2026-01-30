from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.book import (
    BookCreate,
    BookRead,
    BookUpdate,
)
from app.services.book import BookService
from app.api.deps import get_current_user
from app.models.user import User

router = APIRouter(prefix="/books")


@router.post("/", response_model=BookRead, status_code=status.HTTP_201_CREATED)
def create_book(
    book_in: BookCreate,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):
    return BookService().create_book(db, book_in)


@router.get("/", response_model=list[BookRead])
def list_books(
    db: Session = Depends(get_db),
):
    return BookService().list_books(db)


@router.get("/{book_id}", response_model=BookRead)
def get_book(
    book_id: int,
    db: Session = Depends(get_db),
):
    book = BookService().get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.put("/{book_id}", response_model=BookRead)
def update_book(
    book_id: int,
    book_in: BookUpdate,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):
    service = BookService()
    book = service.get_book(db, book_id)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    return service.update_book(db, book, book_in)


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(
    book_id: int,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):
    service = BookService()
    book = service.get_book(db, book_id)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    service.delete_book(db, book)
