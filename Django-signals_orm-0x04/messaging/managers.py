from django.db import models

class UnreadMessagesManager(models.Manager):
    def unread_for_user(self, user):
        """
        Return unread messages for the given user, optimized with .only().
        """
        return (
            self.filter(receiver=user, read=False)
            .only('id', 'sender', 'receiver', 'content', 'timestamp')
            .select_related('sender', 'receiver')
        )
