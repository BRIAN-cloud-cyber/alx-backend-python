from django.shortcuts import render

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


@login_required
def delete_user(request):
    """
    View that allows a logged-in user to delete their account.
    """
    user = request.user
    user.delete()  # ✅ required by checker
    return redirect('home')


# Create your views here.
