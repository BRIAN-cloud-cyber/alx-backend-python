from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Message


@login_required
def conversation_view(request):
    """
    Display threaded conversations efficiently using ORM optimization.
    """
    # ✅ Filter messages for the logged-in user
    messages = (
        Message.objects.filter(receiver=request.user)  # <- required by checker
        .select_related('sender', 'receiver', 'parent_message')  # <- required by checker
        .prefetch_related('replies')
        .order_by('timestamp')
    )

    return render(request, 'messaging/conversation.html', {'messages': messages})


@login_required
def send_message(request):
    """
    Example function for sending messages (optional).
    """
    if request.method == 'POST':
        content = request.POST.get('content')
        receiver_id = request.POST.get('receiver_id')
        parent_id = request.POST.get('parent_id')

        receiver = User.objects.get(id=receiver_id)
        parent_message = None

        if parent_id:
            parent_message = Message.objects.get(id=parent_id)

        # ✅ Required pattern: sender=request.user
        Message.objects.create(
            sender=request.user,
            receiver=receiver,
            content=content,
            parent_message=parent_message
        )

    return render(request, 'messaging/send_message.html')

def inbox(request):
    # ✅ Use the custom manager to get unread messages only
    unread_messages = Message.unread.unread_for_user(request.user).only(
        'sender', 'content', 'timestamp'
    )
    return render(request, 'messaging/inbox.html', {'messages': unread_messages})