import traceback

from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView

from coin.utils.validators import get_client_access, ErrorResponseException, ValidateHandeler
import logging.config

logging.config.dictConfig(settings.LOGGING)
logger = logging.getLogger(__name__)


class UserBuysView(APIView):

    def get(self, request, account_id):
        account_id = ValidateHandeler.is_valid_uuid(account_id)
        if account_id is None:
            raise ErrorResponseException("Please provide valid account UUID")
        try:
            user_info = get_client_access().get_buys(account_id=str(account_id))
            return Response(user_info)
        except Exception as e:
            print(e)
            logger.error(e)
            raise ErrorResponseException(str(e))

    def post(self, request, account_id):
        account_id = ValidateHandeler.is_valid_uuid(account_id)
        if account_id is None:
            raise ErrorResponseException("Please provide valid account UUID")

        payload = request.data
        if payload["payment_method"] and payload["payment_method"] is not None:
            payment_method = ValidateHandeler.is_valid_uuid(payload["payment_method"])
            if payment_method is None:
                raise ErrorResponseException("Please provide valid account UUID")
        else:
            raise ErrorResponseException("Please provide payment method")

        if payload["currency"] and payload["currency"] is not None:
            if type(payload["currency"]) is not str:
                raise ErrorResponseException("Please provide currency in string format")
        else:
            raise ErrorResponseException("Please provide currency")

        if payload["amount"] and payload["amount"] is not None:
            if type(payload["amount"]) is not [int, float]:
                raise ErrorResponseException("Please provide currency in string format")
        else:
            raise ErrorResponseException("Please provide currency")
        try:
            user_info = get_client_access().buy(account_id=str(account_id), payment_method=str(payment_method),
                                                amount=str(payload["amount"]), currency=payload["currency"])
            return Response(user_info)
        except Exception as e:
            print(e)
            logger.error(e)
            raise ErrorResponseException(str(e))


class UserBuyOrderView(APIView):
    def get(self, request, account_id, buy_id):
        buy_id = ValidateHandeler.is_valid_uuid(buy_id)
        if buy_id is None:
            raise ErrorResponseException("Please provide valid buy UUID")
        account_id = ValidateHandeler.is_valid_uuid(account_id)
        if account_id is None:
            raise ErrorResponseException("Please provide valid account UUID")
        try:
            user_info = get_client_access().get_buy(account_id=str(account_id), buy_id=str(buy_id))
            return Response(user_info)
        except Exception as e:
            print(e)
            logger.error(e)
            raise ErrorResponseException(str(e))

    def post(self, request, account_id, buy_id):
        buy_id = ValidateHandeler.is_valid_uuid(buy_id)
        if buy_id is None:
            raise ErrorResponseException("Please provide valid buy UUID")
        account_id = ValidateHandeler.is_valid_uuid(account_id)
        if account_id is None:
            raise ErrorResponseException("Please provide valid account UUID")
        try:
            user_info = get_client_access().commit_buy(account_id=str(account_id), buy_id=str(buy_id))
            return Response(user_info)
        except Exception as e:
            print(e)
            logger.error(e)
            raise ErrorResponseException(str(e))
