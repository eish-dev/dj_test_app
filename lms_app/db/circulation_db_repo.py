import datetime
from lms_app.exceptions import ActiveCheckoutFoundException, ActiveCheckoutNotFoundException
from lms_app.models import Circulation
from lms_app.types.circulation_types import CirculationDomainModel
from lms_app.db.books_db_repo import BooksDBRepo
import datetime

class CirculationDBRepo:
    @staticmethod
    def _get_active_circulation(book_id: int, member_id: int) -> Circulation:
        return Circulation.objects.filter(
            is_active=True,
            book__id=book_id,
            member__id=member_id
        ).first()

    @staticmethod
    def save_checkout(circulation_dm: CirculationDomainModel):
        # check if an active circulation exist for book_id and member_id
        # if it does then raise exception

        circulation = CirculationDBRepo._get_active_circulation(
            circulation_dm.book_id, circulation_dm.member_id
        )

        if circulation:
            raise ActiveCheckoutFoundException()

        # else save checkout in circulation object
        circulation = Circulation(
            book_id=circulation_dm.book_id,
            member_id=circulation_dm.member_id,
            is_active=True,
            issue_date=circulation_dm.issue_date,
        )
        circulation.save()


    @staticmethod
    def save_returns(circulation_dm: CirculationDomainModel):

        circulation = CirculationDBRepo._get_active_circulation(
            circulation_dm.book_id, circulation_dm.member_id
        )

        if not circulation:
            raise ActiveCheckoutNotFoundException()

        circulation.return_date = circulation_dm.return_date
        circulation.is_active = False
        circulation.save()

    @staticmethod
    def get_circulations_by_member(member_id):
        circulations = Circulation.objects.filter(is_active=True, member__id=member_id).all()
        circulations_dm_list = [CirculationDomainModel.from_orm(circulation) for circulation in circulations]
        return circulations_dm_list

