from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes


@api_view(["DELETE"])
# Create your views here.
def delete_user_messages(request):
    user = request.user
    user.received_messages.all().delete()
    user.sent_messages.all().delete()
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
