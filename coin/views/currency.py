import traceback

from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView

from coin.utils.validators import get_client_access, ErrorResponseException, ValidateHandeler
import logging.config

logging.config.dictConfig(settings.LOGGING)
logger = logging.getLogger(__name__)


class ListCurrencyDetails(APIView):

    def get(self, request):
        try:
            user_info = get_client_access().get_currencies()
            return Response(user_info)
        except Exception as e:
            print(e)
            logger.error(e)
            raise ErrorResponseException(str(e))
