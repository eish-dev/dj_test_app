from lms_app.db.books_db_repo import BooksDBRepo
from lms_app.db.circulation_db_repo import CirculationDBRepo
from lms_app.db.reservation_db_repo import ReservationDBRepo
from lms_app.exceptions import BookNotAvailableException
from lms_app.types.circulation_types import CirculationDomainModel, ReservationDomainModel



class CirculationService:
    def __init__(self):
        self.books_db_repo = BooksDBRepo()
        self.circulation_db_repo = CirculationDBRepo()
        self.reservation_db_repo = ReservationDBRepo()

    def checkout_book(self, circulation_dm: CirculationDomainModel):
        book = self.books_db_repo.get_by_id(circulation_dm.book_id)
        # get cached book
        if book.available_copies:
            self.books_db_repo.update_available_copies(book_id=book.id, copies=(book.available_copies-1))
            self.circulation_db_repo.save_checkout(circulation_dm=circulation_dm)
        else:
            self.reservation_db_repo.add_reservation(
                ReservationDomainModel(
                    book_id=circulation_dm.book_id,
                    member_id=circulation_dm.member_id,
                    is_active=True
                )
            )

    def return_book(self, circulation_dm: CirculationDomainModel):
        self.circulation_db_repo.save_returns(circulation_dm)
        book = self.books_db_repo.get_by_id(circulation_dm.book_id)
        self.books_db_repo.update_available_copies(book_id=book.id, copies=(book.available_copies + 1))


    def fulfil_reservation(self, book_id, date):
        latest_reservation = self.reservation_db_repo.get_latest_reservation(book_id)
        circulation_dm = CirculationDomainModel(book_id=book_id, issue_date=date, member_id=latest_reservation.member_id)
        reservation_dm = ReservationDomainModel(book_id=latest_reservation.book_id, member_id=latest_reservation.member_id, is_active=False)
        self.reservation_db_repo.update_reservation(reservation_dm)
        self.checkout_book(circulation_dm)



circulation_service = CirculationService()