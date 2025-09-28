from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import message,conversation
from .serializers import messageSerializer,conversationSerializer
from .permissions import IsParticipantOfConversation
from .filters import MessageFilter


class MessageViewSet(viewsets.ModelViewSet):
    queryset=message.objects.all()
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


from django.http import HttpResponse
def index(request):
    return HttpResponse("welcome to the chats app")

def room(requestx,room_id):
    return HttpResponse(f"This is chat room {room_id}")



