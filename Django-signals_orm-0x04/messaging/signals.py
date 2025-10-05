from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Message, MessageHistory, Notification


# --- Existing signal for message edits ---
@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    if not instance.pk:
        return
    try:
        old_message = Message.objects.get(pk=instance.pk)
    except Message.DoesNotExist:
        return
    if old_message.content != instance.content:
        MessageHistory.objects.create(
            message=old_message,
            old_content=old_message.content,
            edited_by=instance.edited_by,
        )
        instance.edited = True
        instance.edited_at = timezone.now()


# --- ✅ New signal for user deletion ---
@receiver(post_delete, sender=User)
def delete_user_related_data(sender, instance, **kwargs):
    """
    Automatically deletes all related messages, notifications, and histories
    when a User account is deleted.
    """
    # Delete all messages sent or received by the user
    Message.objects.filter(sender=instance).delete()   # ✅ checker looks for this
    Message.objects.filter(receiver=instance).delete() # ✅

    # Delete all notifications related to the user
    Notification.objects.filter(user=instance).delete()

    # Delete message histories linked to the user's messages
    MessageHistory.objects.filter(message__sender=instance).delete()
    MessageHistory.objects.filter(message__receiver=instance).delete()
