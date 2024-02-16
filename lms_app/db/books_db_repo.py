from lms_app.models import Books
from lms_app.types.books_types import BookDomainModel


class BooksDBRepo:

    @staticmethod
    def get_by_id(book_id: int) -> BookDomainModel:
        book = Books.objects.filter(id=book_id)

        return BookDomainModel.from_orm(book.get())

    @staticmethod
    def update_available_copies(book_id: int, copies: int) -> None:
        book = Books.objects.get(id=book_id)
        book.available_copies = copies
        book.save()

        
