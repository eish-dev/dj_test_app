from django.db import transaction
from rest_framework.response import Response
from rest_framework.views import APIView
from django.forms.models import model_to_dict

from lms_app.exceptions import BookNotAvailableException
from rest_framework.decorators import api_view
from lms_app.services.circulation_service import circulation_service
from lms_app.types.circulation_types import CirculationDomainModel
from lms_app.services.overdue_service import overdue_service



@transaction.atomic
@api_view(['POST'])
def handle_event(request):
    book_id = int(request.data.get('book_id'))
    member_id = int(request.data.get('member_id'))
    date = request.data.get('date')
    event_type = request.data.get('eventtype')
    circulation_dm = CirculationDomainModel(member_id=member_id, book_id=book_id, issue_date=date)
    if event_type == 'checkout':
        # checkout_book(request)
        circulation_service.checkout_book(circulation_dm)
        return Response({'message': 'success'})
    if event_type == 'return':
        circulation_service.return_book(circulation_dm)
        return Response({'message': 'success, book returned successfuly'})
    if event_type == 'fulfil':
        fulfil_request = circulation_service.fulfil_reservation(book_id, date)


@transaction.atomic
@api_view(['POST'])
def checkout_book(request):
    book_id = int(request.data.get('book_id'))
    member_id = int(request.data.get('member_id'))
    date = request.data.get('date')
    circulation_dm = CirculationDomainModel(member_id=member_id, book_id=book_id, issue_date=date)
    try:
        circulation_service.checkout_book(circulation_dm)
        return Response({'message': 'success'})
    except BookNotAvailableException:
        return Response({'error': 'book not available'}, status=404)


@transaction.atomic
@api_view(['POST'])
def return_book(request):
    book_id = int(request.data.get('book_id'))
    member_id = int(request.data.get('member_id'))
    date = request.data.get('date')
    circulation_dm = CirculationDomainModel(member_id=member_id, book_id=book_id, return_date=date)
    circulation_service.return_book(circulation_dm)
    return Response({'message': 'success, book returned successfuly'})


@api_view(['POST'])
def get_overdues(request):
    member_id = int(request.data.get('member_id'))
    overdue_books = overdue_service.get_overdue_books(member_id)

    return Response({'overdue_books': overdue_books})


@api_view(['POST'])
def fulfil_reservation(request):
    book_id = int(request.data.get('book_id'))
    date = request.data.get('date')
    fulfil_request = circulation_service.fulfil_reservation(book_id, date)

    return Response({'overdue_books': fulfil_request})
