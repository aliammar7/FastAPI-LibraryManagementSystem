from sqlalchemy.orm import Session

from app.models.book import Book
from app.schemas.book import BookCreate, BookUpdate
from app.repositories.book import BookRepository


class BookService:
    def __init__(self) -> None:
        self.repo = BookRepository()

    def create_book(self, db: Session, book_in: BookCreate) -> Book:
        book = Book(
            title=book_in.title,
            author=book_in.author,
            isbn=book_in.isbn,
        )
        return self.repo.create(db, book)

    def get_book(self, db: Session, book_id: int) -> Book | None:
        return self.repo.get_by_id(db, book_id)

    def list_books(self, db: Session) -> list[Book]:
        return self.repo.get_all(db)

    def update_book(
        self,
        db: Session,
        book: Book,
        book_in: BookUpdate,
    ) -> Book:
        if book_in.title is not None:
            book.title = book_in.title
        if book_in.author is not None:
            book.author = book_in.author

        return self.repo.update(db, book)

    def delete_book(self, db: Session, book: Book) -> None:
        self.repo.delete(db, book)

    def assign_owner(
        self,
        db: Session,
        book: Book,
        user_id: int,
    ) -> Book:
        book.owner_id = user_id
        return self.repo.update(db, book)

    def remove_owner(self, db: Session, book: Book) -> Book:
        book.owner_id = None
        return self.repo.update(db, book)
