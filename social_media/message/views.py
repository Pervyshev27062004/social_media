import logging
from django.shortcuts import render, redirect
from message.models import Message
from message.forms import AddMessageForm
from django.views.generic import ListView

logger = logging.getLogger(__name__)


class MessageListView(ListView):
    model = Message
    template_name = 'messages.html'
    context_object_name = 'messages'
    ordering = ['date_posted']
    paginate_by = 10


def post_message(request):
    if request.method == "POST":
        form = AddMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('message')
    form = AddMessageForm()

    data = {
        'form': form
    }
    return render(request, "add_message.html", data)
