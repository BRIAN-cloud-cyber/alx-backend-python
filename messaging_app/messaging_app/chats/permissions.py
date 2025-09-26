from rest_framework.permissions import BasePermission,IsAuthenticated

class IsParticipantOfConversation(BasePermission):
    """
    - custom permission
    - only allow autenticated users
    -only allow participants of a conversation to send/view/update/delete messages
    """

    def has_permission(self, request, view):
        return super().has_permission(request, view)
    
    def has_object_permission(self, request, view, obj):

        if hasattr(obj,"participants"):

            return request.user in obj.participants.all
        if hasattr(obj,"sender") and hasattr(obj,"receiver"):
            return obj.sender ==request.user or obj.receiver ==request.user
        
        return False 