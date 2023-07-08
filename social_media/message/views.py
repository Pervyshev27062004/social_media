import logging
from django.shortcuts import render
from message.models import Message

logger = logging.getLogger(__name__)


def post_message(request):
    context = {
        'messages': Message.objects.all()
    }
    return render(request, 'messages.html', context)
