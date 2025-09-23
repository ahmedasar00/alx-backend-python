from rest_framework import viewsets
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer


class ConversationFilter(viewsets.ModelViewSet):
    """
    ViewSet to handle conversations.
    """

    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer


class MessageFilter(viewsets.ModelViewSet):
    """
    ViewSet to handle messages.
    """

    queryset = Message.objects.all()
    serializer_class = MessageSerializer
