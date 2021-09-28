from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from coinbase.wallet.client import Client
from django.conf import settings
import logging.config
from coin.utils.validators import ErrorResponseException, get_client_access, ValidateHandeler
logging.config.dictConfig(settings.LOGGING)
logger = logging.getLogger(__name__)


class CurrentUserDetailsView(APIView):

    """
    To get current user details and update the user.
    """

    def get(self, request):
        try:
            user_info = get_client_access().get_current_user()
            return Response(user_info)

        except Exception as e:
            print(e)
            logger.error(e)
            raise ErrorResponseException(str(e))

    def put(self, request):
        payload = request.data
        if "name" in payload and type(payload.get("name")) is not str:
            raise ErrorResponseException("Provided name should be in string format")
        try:
            user = get_client_access().update_current_user(name=payload.get("name"))
            return Response(user)

        except Exception as e:
            print(e)
            logger.error(e)
            raise ErrorResponseException(str(e))


class UserDetailsView(APIView):

    """
    To get the user details by user id.
    """

    def get(self, request, user_id):
        user_id = ValidateHandeler.is_valid_uuid(user_id)
        if user_id is None:
            raise ErrorResponseException("Please provide valid user UUID")
        try:
            user_info = get_client_access().get_user(user_id=str(user_id))
            return Response(user_info)

        except Exception as e:
            print(e)
            logger.error(e)
            raise ErrorResponseException(str(e))


class UserAuthView(APIView):

    """
    To get user authorize app's.
    """

    def get(self, request):
        try:
            user_auth = get_client_access().get_auth_info()
            return Response(user_auth)

        except Exception as e:
            print(e)
            logger.error(e)
            raise ErrorResponseException(str(e))
