from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .models import Message
from .serializers import MessageSerializer

from rest_framework.generics import ListAPIView

User = get_user_model()


@api_view(["DELETE"])
# Create your views here.
def delete_user_messages(request):
    user = request.user
    # user.received_messages.all().delete()
    # user.sent_messages.all().delete()
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


class ThreadedConversation(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        queryset = (
            Message.objects.filter(reverser=request.user, parent_message__isnull=True)
            .select_related("sender")
            .prefetch_related("replies__sender")
        )
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        try:
            hypothetical_message = Message.objects.exclude(pk=request.user.pk).first()
            if not hypothetical_message:
                return Response(
                    {"Error: No Other User Exists"}, status=status.HTTP_400_BAD_REQUEST
                )
            Message.objects.create(
                sender=request.user,
                receiver=hypothetical_message.receiver,
                content=request.data.get("content", ""),
            )
            return Response({"Success: Message Sent"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
