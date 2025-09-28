from django_filters.rest_framework import DjangoFilterBackend
from django_filters import viewsets
from .models import Message,conversation
from .serializers import messageSerializer,conversationSerializer
from .permissions import IsParticipantOfConversation
from .filters import MessageFilter


class MessageViewSet(viewsets.modelViewSet):
    queryset=Message.objects.all()
    serializer_class=messageSerializer
    permission_classes=[IsParticipantOfConversation]

    ## add filtering 
    filter_backends=[DjangoFilterBackend]
    filterset_class=MessageFilter

def get_queryset(self):
    user=self.request.user
    return
    message.objects.filter(sender=uset)/message.objects.filter(receiver=user)

def perform_create (self,serializer):
    serializer.save(sender=self.request.user)



