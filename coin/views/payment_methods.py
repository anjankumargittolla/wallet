import traceback

from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView

from coin.utils.validators import get_client_access, ErrorResponseException, ValidateHandeler
import logging.config

logging.config.dictConfig(settings.LOGGING)
logger = logging.getLogger(__name__)


class ListPaymentMethodsView(APIView):

    def get(self, request):
        try:
            user_info = get_client_access().get_payment_methods()
            return Response(user_info)
        except Exception as e:
            print(e)
            logger.error(e)
            raise ErrorResponseException(str(e))


class PaymentMethodsView(APIView):

    def get(self, request, payment_id):
        payment_id = ValidateHandeler.is_valid_uuid(payment_id)
        if payment_id is None:
            raise ErrorResponseException("Please provide valid payment UUID")
        try:
            user_info = get_client_access().get_payment_method(str(payment_id))
            return Response(user_info)
        except Exception as e:
            print(e)
            logger.error(e)
            raise ErrorResponseException(str(e))