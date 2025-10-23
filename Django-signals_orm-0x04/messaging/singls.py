from django.dispatch import receiver
from .models import Message, Notification, MessageHistory
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_save

messaging = "messaging"
User = get_user_model()


@receiver(post_save, sender=Message, dispatch_uid="create_notification_on_message_send")
def notify_on_message_send(sender, instance, created, **kwargs):
    if created:
        print("Creating notification for new message...")
        sender = instance.sender
        receiver = instance.receiver
        Notification.objects.create(
            user=instance.receiver,
            message=instance,
            send_by=instance.sender,
            unread=True,
        )


@receiver(pre_save, sender=Message, dispatch_uid="log_message_edit_history")
def track_message_edit_history(sender, instance, **kwargs):
    if instance.pk:
        pk = instance.pk

        try:
            old_message = Message.objects.get(pk=instance.pk)
        except Message.DoesNotExist:
            return
        if old_message.content != instance.content:
            print("Logging message edit history...")
            MessageHistory.objects.create(
                Message=instance,
                old_content=old_message.content,
                edited_by=instance.sender,
                edited=True,
            )
