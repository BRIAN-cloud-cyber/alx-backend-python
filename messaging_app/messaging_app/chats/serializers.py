from rest_framework import serializers
from .models import message,conversation
class messageSerializer(serializers.ModelSerializer):
    class Meta:
        model=message
        fields='__all__'

class conversationSerializer(serializers.ModelSerializer):
    # show related messages inside a conversation:

    messages=messageSerializer(many=True,read_only=True)
    class Meta:
        model=conversation
        fields='__all__'
        
