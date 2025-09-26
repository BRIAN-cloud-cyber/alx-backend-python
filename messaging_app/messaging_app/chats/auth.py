from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class messagingView(APIView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    permission_classes=[IsAuthenticated]

    def get(self,requestc,format=None):
        request={

            'user':str(request.user),
            'auth':str(request.auth),
        }

        return Response (request)