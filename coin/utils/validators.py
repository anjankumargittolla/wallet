import uuid
import re

from coinbase.wallet.client import Client
from django.conf import settings
from django.core.validators import validate_email
from rest_framework import status
from rest_framework.exceptions import APIException, ValidationError

from coin.utils import make_error_response_dict


def get_client_access():
    api_key, api_secret = settings.COINBASE_API_KEY, settings.COINBASE_SECRET_KEY
    if api_key is None and api_secret is None:
        raise ErrorResponseException("Please provide valid tokens")
    client = Client(api_key, api_secret)
    return client


class ErrorResponseException(APIException):

    '''
    return http response in the format {"error": {
        "message": "some message"}}
    '''
    def __init__(self, message, status_code=status.HTTP_400_BAD_REQUEST):
        self.detail = make_error_response_dict(message)
        self.status_code = status_code


class ValidateHandeler:
    @staticmethod
    def is_valid_uuid(val):
        try:
            return uuid.UUID(str(val))
        except ValueError:
            return None

    @staticmethod
    def validateEmail(email):

        try:
            validate_email(email)
            return True
        except ValidationError:
            return False

    @staticmethod
    def validatePhNumber(phno):
        phno_check = re.compile(r"^\+?1?\d{9,15}$")
        if phno_check.search(phno) is None:
            return False
        else:
            return True
