from lms_app.exceptions import ReservationAlreadyExistsException, ReservationNotAvailableException
from lms_app.models import ReservationQueue
from lms_app.types.circulation_types import ReservationDomainModel


class ReservationNotFoundException:
    pass


class ReservationDBRepo:

    @staticmethod
    def _get_active_reservations(book_id, member_id):
        return ReservationQueue.objects.filter(
            is_active=True,
            book__id=book_id,
            member__id=member_id
        ).first()

    @staticmethod
    def add_reservation(reservation_dm: ReservationDomainModel):
        reservation = ReservationDBRepo._get_active_reservations(reservation_dm.book_id, reservation_dm.member_id)
        if reservation:
            raise ReservationAlreadyExistsException()
        reservation = ReservationQueue(
            book_id=reservation_dm.book_id,
            member_id=reservation_dm.member_id,
            is_active=True,
        )

        reservation.save()

    @staticmethod
    def update_reservation(reservation_dm: ReservationDomainModel):
        reservation = ReservationDBRepo._get_active_reservations(reservation_dm.book_id, reservation_dm.member_id)
        if not reservation:
            raise ReservationNotAvailableException()
        reservation.is_active = reservation_dm.is_active
        reservation.save()

    @staticmethod
    def get_latest_reservation(book_id: int) -> ReservationDomainModel:
        # get reservation for this book with is_active=True and sorted in asc on created_at
        reservation = ReservationQueue.objects.filter(
            is_active=True, book_id=book_id
        ).order_by('-created_at').first()

        return ReservationDomainModel.from_orm(reservation)



