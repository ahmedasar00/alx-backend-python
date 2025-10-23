from django.db import models


class UnreadMessagesQuerySet(models.QuerySet):
    def unread_for_user(self, user):
        return self.filter(receiver=user, read=False)


class UnreadMessagesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(read=False)

    def unread_for_user(self, user):
        return self.get_queryset().filter(receiver=user)
