from rest_framework.permissions import BasePermission


class IsMessageOwner(BasePermission):
    """
    custom permission:only sender or receiver can view/edit a message 
    """

    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj)
    


    #conversation permission

    class IsConversationParticipant(BasePermission):
        """
        custom permission:only participants can access the conversion.
        """
        def has_object_permission(self, request, view, obj):
            return super().has_object_permission(request, view, obj)
        