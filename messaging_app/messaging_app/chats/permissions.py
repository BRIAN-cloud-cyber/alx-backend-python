from rest_framework.permissions import BasePermission,SAFE_METHODS

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

        # check if user belongs to this conversation 
            in_conversation=request.user in [obj.sender,obj.receiver]
             
        if request.method in SAFE_METHODS:
            #GET,HEAD,OPTIONS

            return in_conversation
        
        if request.method in ["PUT","PATCH","DELETE"]:
            # only the sender can edir pr delete

            return obj.sender ==request.user 
        return in_conversation
    
