from django.forms import ModelForm, TextInput
from message.models import Message


class AddMessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['message', 'author']

        widgets = {
            'message': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Написать сообщение'
            }),

        }
