from django.db import models

# Create your models here.
from django.conf import settings
from .managers import UnreadMessageManager


class Message(models.Model):
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sent_messages"
    )
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="received_messages",
    )
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    unread = UnreadMessageManager()  # Custom manager for unread messages.
    objects = models.Manager()  # The default manager.

    def __str__(self):
        return f"Message from {self.sender} to {self.receiver} at {self.timestamp}"


class Notification(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notifications"
    )
    message = models.ForeignKey(
        Message, on_delete=models.CASCADE, related_name="notifications"
    )
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    send_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sent_notifications",
    )

    def __str__(self):
        return f"Notification for {self.user} about message {self.message.id}"


class MessageHistory(models.Model):
    edited = models.BooleanField(default=False)
    Message = models.ForeignKey(
        Message, on_delete=models.CASCADE, related_name="history"
    )
    old_content = models.TextField(max_length=10000, blank=False)
    edited_at = models.DateTimeField(auto_now_add=True)
    edited_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="eddited_history",
    )
