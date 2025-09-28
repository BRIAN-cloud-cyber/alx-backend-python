import logging
from datetime import datetime,timedelta

from django.Http import HttpResponseForbidden

class RequestLoggingMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        logging.basicConfig(

            filename='requests.log',
            level=logging.INFO
            format="%(message)s"
        )

    def __call__(self,request):
        user=request.user if request.user.is_authenticated else
        "Anonymous"
        log_message=f"{datetime.now()}-user:{user}-path:{request.path}"
        logging.info(log_message)

        response=self.get_response(request)
        return response
    
class RestrictAccessByTimeMiddleware:
    def __init__ (self,get_response):
        self.get_response=get_response

    def __call__ (self,request):
        now=datetime.now().hour

        if now < 18 or now > 21 : # only allows between 18:00 and 21:00
            return HttpResponseForbidden("chat is only available between 6 pm and 9 pm")
        response=self.get_response(request)
        return response
    

class OffensiveLanguageMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        self.ip_requests={}

    def __call__(self, request):
        if request.method == "POST":
            ip = self.get_client_ip(request)
            now=datetime.now ()

            if ip not in self.ip_requests:
                self.ip_requests[ip]=[]

                # clean old requests

            self.ip_requests[ip]=[t for t in self.ip_requests[ip]
                                  if now - t <timedelta(minutes=1)]

            if len(self.ip_requests[ip]) >=5:
                return
            HttpResponseForbidden("rate limit exceeded.Try again later.")

            self.ip_requests[ip].append(now)
            response=self.get_response(request)
            return response
    def get_client_ip(self,request):
        # x-forwarded - for is used f behind proxy

        x_forwarded_for=request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            return x_forwarded_for.split(",")[0]
        return
        request.META.get("REMOTE_ADDR")
    


class RolePermissionMiddleware:
     
    def __init__ (self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        if request.user.is_authenticated:
            user_role=getattr(request.user,"role",None) # assume user has a role

            if user_role not in ['admin','moderator']:
                return HttpResponseForbidden ("you do not have permission to perform this action")
            
            response=self.get_response(request)
            return response

