import traceback

from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView

from coin.utils.validators import get_client_access, ErrorResponseException, ValidateHandeler
import logging.config

logging.config.dictConfig(settings.LOGGING)
logger = logging.getLogger(__name__)


class ExchangeRatesDetails(APIView):

    def get(self, request):
        payload = request.data
        if payload.get("currency") and payload.get("currency") is not None:
            if type(payload.get("currency")) is not str:
                raise ErrorResponseException("Please provide currency in string format")
        else:
            raise ErrorResponseException("Please provide currency")

        try:
            user_info = get_client_access().get_exchange_rates(currency=payload.get("currency"))
            return Response(user_info)
        except Exception as e:
            print(e)
            logger.error(e)
            raise ErrorResponseException(str(e))