from rest_framework import ModelSerializer, SerializerMethodField
from .models import *
from django.contrib.auth import get_user_model

User = get_user_model()


class MessageSerializer(ModelSerializer):
    sender = SerializerMethodField()
    reciver = SerializerMethodField

    class Meta:
        model = Message
        fields = "__all__"

        def get_sender(self, obj):
            return obj.sender.username

        def get_reciver(self, obj):
            return obj.reciver.username
