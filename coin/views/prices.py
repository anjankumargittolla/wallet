import traceback

from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView

from coin.utils.validators import get_client_access, ErrorResponseException, ValidateHandeler
import logging.config

logging.config.dictConfig(settings.LOGGING)
logger = logging.getLogger(__name__)


class UserBuyPrice(APIView):

    def get(self, request):
        payload = request.data
        if payload.get("currency_pair") and payload.get("currency_pair") is not None:
            if type(payload.get("currency_pair")) is not str:
                raise ErrorResponseException("Please provide currency in string format")
        else:
            raise ErrorResponseException("Please provide currency pair")
        try:
            user_info = get_client_access().get_buy_price(currency_pair=payload.get("currency_pair") )
            return Response(user_info)
        except Exception as e:
            print(e)
            logger.error(e)
            raise ErrorResponseException(str(e))


class UserSellPrice(APIView):

    def get(self, request):
        payload = request.data
        if payload.get("currency_pair") and payload.get("currency_pair") is not None:
            if type(payload.get("currency_pair")) is not str:
                raise ErrorResponseException("Please provide currency in string format")
        else:
            raise ErrorResponseException("Please provide currency pair")
        try:
            user_info = get_client_access().get_sell_price(currency_pair=payload.get("currency_pair") )
            return Response(user_info)
        except Exception as e:
            print(e)
            logger.error(e)
            raise ErrorResponseException(str(e))


class UserSpotPrice(APIView):

    def get(self, request):
        payload = request.data
        if payload.get("currency_pair") and payload.get("currency_pair") is not None:
            if type(payload.get("currency_pair")) is not str:
                raise ErrorResponseException("Please provide currency in string format")
        else:
            raise ErrorResponseException("Please provide currency pair")
        try:
            user_info = get_client_access().get_spot_price(currency_pair=payload.get("currency_pair") )
            return Response(user_info)
        except Exception as e:
            print(e)
            logger.error(e)
            raise ErrorResponseException(str(e))