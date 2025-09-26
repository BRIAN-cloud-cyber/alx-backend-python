from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser


from django.conf import settings



class User(AbstractUser):
    id=models.UUIDField(primary_key=True,
    default=uuid.uuid4,editable=False)

    phone_number=models.CharField(max_length=20,blank=True,null=True)
    role=models.CharField(max_length=10,
                          choices=[('guest','Guest'),
                                   ('host','Host'),
                                   ('admin','Admin'),
                                   ],

                                   default='guest'
                                   )
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username}({self.role})"
    

class conversation(models.Model):
    id=models.UUIDField(primary_key=True,
                        default=uuid.uuid4,editable=False)
    participants=models.ManyToManyField(User,related_name="conversations")

    created_at=models.DateTimeField ()


# Create your models here.
class message (models.Model):
    sender=models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name="sent_message")
    
    receiver=models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name="received_messages")
    
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)
    is_read=models.BooleanField(default=False)

    def __str__(self):
        return f" From{self.sender} to {self.receiver}:{self.content[:30]}"

