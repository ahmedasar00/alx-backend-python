from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404

from .models import Conversation, Message, User
from .serializers import ConversationSerializer, MessageSerializer
from .permissions import IsParticipantOfConversation
from .filters import ConversationFilter, MessageFilter


# -------------------------------
# Conversation ViewSet
# -------------------------------
class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]
    filter_backends = [filters.SearchFilter]
    search_fields = ["participants__email"]  # search by participant email
    filterset_class = ConversationFilter

    def get_queryset(self):
        """
        Return only the conversations that the current authenticated user participates in.
        """
        return Conversation.objects.filter(participants=self.request.user)

    def create(self, request, *args, **kwargs):
        """
        Create a new conversation with a list of participant IDs.
        Example payload:
        {
            "participants": ["uuid1", "uuid2"]
        }
        """
        participant_ids = request.data.get("participants", [])
        if not participant_ids:
            return Response(
                {"error": "At least one participant is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        conversation = Conversation.objects.create()
        conversation.participants.set(User.objects.filter(user_id__in=participant_ids))

        # Add the current user automatically to the conversation
        conversation.participants.add(request.user)

        serializer = self.get_serializer(conversation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=["get"])
    def messages(self, request, pk=None):
        """
        Custom endpoint: Get all messages in a conversation.
        """
        conversation = self.get_object()

        # Ensure the current user is a participant
        if request.user not in conversation.participants.all():
            raise PermissionDenied("You are not a participant in this conversation.")

        messages = conversation.messages.all().order_by("-timestamp")  # newest first
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)


# -------------------------------
# Message ViewSet
# -------------------------------
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]
    filter_backends = [filters.SearchFilter]
    search_fields = ["message_body", "sender__email"]
    filterset_class = MessageFilter
    ordering_fields = ["timestamp"]
    ordering = ["-timestamp"]  # newest message first

    def get_queryset(self):
        """
        Return only messages for the conversation specified in the URL.
        """
        conversation_pk = self.kwargs["conversation_pk"]
        conversation = get_object_or_404(Conversation, pk=conversation_pk)

        # Ensure the user is a participant
        if self.request.user not in conversation.participants.all():
            raise PermissionDenied("You are not a participant in this conversation.")

        return Message.objects.filter(conversation=conversation)

    def perform_create(self, serializer):
        """
        Automatically set the conversation and sender for a new message.
        """
        conversation = get_object_or_404(
            Conversation, pk=self.kwargs["conversation_pk"]
        )
        if self.request.user not in conversation.participants.all():
            raise PermissionDenied("You are not a participant in this conversation.")

        serializer.save(conversation=conversation, sender=self.request.user)
