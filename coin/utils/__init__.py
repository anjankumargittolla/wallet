from rest_framework import status
from rest_framework.response import Response


def make_error_response_dict(message):
    return {"error": {"message": message}}


def send_error_response(message, status=status.HTTP_400_BAD_REQUEST):
    return Response(make_error_response_dict(message), status=status)
