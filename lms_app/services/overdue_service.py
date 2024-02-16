from datetime import datetime, timedelta

from lms_app.db.books_db_repo import BooksDBRepo
from lms_app.db.circulation_db_repo import CirculationDBRepo
from lms_app.db.reservation_db_repo import ReservationDBRepo
from lms_app.exceptions import BookNotAvailableException
from lms_app.types.circulation_types import CirculationDomainModel


class OverdueService:
    def __init__(self):
        self.books_db_repo = BooksDBRepo()
        self.circulation_db_repo = CirculationDBRepo()
        self.reservation_db_repo = ReservationDBRepo()


    def get_overdue_books(self, member_id):
        circulations = self.circulation_db_repo.get_circulations_by_member(member_id)
        overdue_books = {}
        for circulation in circulations:
            # for each circulation check circulation.return > datetime(2023-05-31) or return_date=null

            # if circulation.return_date > datetime(2023,5,31) or circulation.return_date is None:
            due_date = circulation.issue_date + timedelta(days=7)
            return_date = circulation.return_date
            today = datetime(2023,5,31)
            if return_date and return_date > due_date:
                overdue_days= return_date - due_date
                overdue_books[circulation.book_id] = {"overdue_days": overdue_days.days, "fine": 50*overdue_days.days}
            if return_date is None:
                overdue_days = abs(today - due_date)
                overdue_books[circulation.book_id] = {"overdue_days": overdue_days.days, "fine": 50 * overdue_days.days}

        return overdue_books




overdue_service = OverdueService()