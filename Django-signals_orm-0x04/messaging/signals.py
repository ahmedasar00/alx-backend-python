from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, pre_delete, post_delete
from .models import Message, Notification, MessageHistory
from django.contrib.auth import get_user_model

User = get_user_model()


@receiver(post_save, sender=Message, dispatch_uid="create_notification_on_message_send")
def notify_on_message_send(sender, instance, created, **kwargs):
    if created:
        print("Creating notification for new message...")
        Notification.objects.create(
            user=instance.receiver,
            message=instance,
            send_by=instance.sender,
            is_read=False,
        )


@receiver(pre_save, sender=Message, dispatch_uid="log_message_edit_history")
def track_message_edit_history(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_message = Message.objects.get(pk=instance.pk)
        except Message.DoesNotExist:
            return
        if old_message.content != instance.content:
            print("Logging message edit history...")
            MessageHistory.objects.create(
                message=instance,
                old_content=old_message.content,
                edited_by=instance.sender,
                edited=True,
            )


@receiver(pre_delete, sender=Message, dispatch_uid="log_message_delete")
def log_message_delete(sender, instance, **kwargs):
    print(f"Message by {instance.sender} to {instance.receiver} is being deleted...")
    MessageHistory.objects.create(
        message=instance,
        old_content=instance.content,
        edited_by=instance.sender,
        edited=True,
    )


@receiver(post_delete, sender=Message, dispatch_uid="delete_related_notifications")
def delete_related_notifications(sender, instance, **kwargs):
    print(f"Deleting all notifications for message {instance.id}...")
    Message.objects.filter(sender=instance).delete()
    Message.objects.filter(receiver=instance).delete()
    Notification.objects.filter(user=instance).delete()
    Notification.objects.filter(send_by=instance).delete()
    MessageHistory.objects.filter(edited_by=instance).delete()
