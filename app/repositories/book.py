from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.book import Book


class BookRepository:
    def get_by_id(self, db: Session, book_id: int) -> Book | None:
        stmt = select(Book).where(Book.id == book_id)
        return db.scalar(stmt)

    def get_all(self, db: Session) -> list[Book]:
        stmt = select(Book)
        return list(db.scalars(stmt))

    def create(self, db: Session, book: Book) -> Book:
        db.add(book)
        db.commit()
        db.refresh(book)
        return book

    def update(self, db: Session, book: Book) -> Book:
        db.add(book)
        db.commit()
        db.refresh(book)
        return book

    def delete(self, db: Session, book: Book) -> None:
        db.delete(book)
        db.commit()
