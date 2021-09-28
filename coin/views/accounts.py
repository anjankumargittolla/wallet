import traceback

from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView

from coin.utils.validators import get_client_access, ErrorResponseException, ValidateHandeler
import logging.config

logging.config.dictConfig(settings.LOGGING)
logger = logging.getLogger(__name__)


class AccountsDetailsView(APIView):

    """
    To get account details of user.
    """

    def get(self, request):
        try:
            user_info = get_client_access().get_accounts()
            return Response(user_info)
        except Exception as e:
            print(e)
            logger.error(e)
            raise ErrorResponseException(str(e))


class AccountDetailsView(APIView):

    """
    To get the details, update, delete the account by passing account id in url.
    """

    def get(self, request, account_id):
        account_id = ValidateHandeler.is_valid_uuid(account_id)
        if account_id is None:
            raise ErrorResponseException("Please provide valid account UUID")
        try:
            user_info = get_client_access().get_account(account_id=str(account_id))
            return Response(user_info)
        except Exception as e:
            print(e)
            logger.error(e)
            raise ErrorResponseException(str(e))

    def put(self, request, account_id):
        payload = request.data
        if account_id is None:
            raise ErrorResponseException("Please provide valid account UUID")
        if "name" in payload and type(payload.get("name")) != str:
            raise ErrorResponseException("Provided name should be in string format")
        # if "primary" in payload and  type(payload.get("primary")) != bool:
        #     raise ErrorResponseException("Provided primary should be in boolean format")
        try:
            user_info = get_client_access().update_account(account_id=str(account_id),
                                                           name=payload.get("name"))
                                                           # primary=payload.get("primary"))
            return Response(user_info)

        except Exception as e:
            print(e)
            logger.error(e)
            raise ErrorResponseException(str(e))

    def delete(self, request, account_id):
        account_id = ValidateHandeler.is_valid_uuid(account_id)
        if account_id is None:
            raise ErrorResponseException("Please provide valid account UUID")
        try:
            user_info = get_client_access().delete_account(account_id=str(account_id))
            return Response(user_info)

        except Exception as e:
            print(e)
            logger.error(e)
            traceback.print_exc()
            raise ErrorResponseException(str(e))
