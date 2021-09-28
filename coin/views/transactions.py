import traceback

from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView

from coin.utils.validators import get_client_access, ErrorResponseException, ValidateHandeler
import logging.config

logging.config.dictConfig(settings.LOGGING)
logger = logging.getLogger(__name__)


class ListTransactionView(APIView):

    def get(self, request, account_id):
        account_id = ValidateHandeler.is_valid_uuid(account_id)
        if account_id is None:
            raise ErrorResponseException("Please provide valid account UUID")
        try:
            user_info = get_client_access().get_transactions(account_id=str(account_id))
            return Response(user_info)
        except Exception as e:
            print(e)
            logger.error(e)
            raise ErrorResponseException(str(e))


class TransactionDetailsView(APIView):

    def get(self, request, account_id, transaction_id):
        transaction_id = ValidateHandeler.is_valid_uuid(transaction_id)
        if transaction_id is None:
            raise ErrorResponseException("Please provide valid transaction UUID")
        account_id = ValidateHandeler.is_valid_uuid(account_id)
        if account_id is None:
            raise ErrorResponseException("Please provide valid account UUID")
        try:
            user_info = get_client_access().get_transaction(account_id=str(account_id), transaction_id=str(transaction_id))
            return Response(user_info)
        except Exception as e:
            print(e)
            logger.error(e)
            raise ErrorResponseException(str(e))

