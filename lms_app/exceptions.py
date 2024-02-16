from rest_framework.exceptions import APIException

class BaseAPIException(APIException):
    status_code = 500
    default_detail = 'A server error occoured'
    default_code = 'SE0001'

    def __init__(self, detail=None, code=None, status_code=None):
        if detail is not None:
            self.detail = detail
        if code is not None:
            self.code = code
        if status_code is not None:
            self.status_code = status_code
        super().__init__(detail, code)


class ActiveCheckoutFoundException(BaseAPIException):
    status_code = 400
    default_detail = 'An active checkout was found'
    default_code = 'AC0001'


class ActiveCheckoutNotFoundException(BaseAPIException):
    status_code = 400
    default_detail = 'No active checkout was found'
    default_code = 'AC0002'


class BookNotAvailableException(BaseAPIException):
    status_code = 400
    default_detail = 'The book is not available'
    default_code = 'BN0001'


class ReservationNotAvailableException(BaseAPIException):
    status_code = 400
    default_detail = 'The reservation is not available'
    default_code = 'RN0001'


class ReservationAlreadyExistsException(BaseAPIException):
    status_code = 400
    default_detail = 'The reservation already exists'
    default_code = 'RE0002'

