from gallery.models import Picture
from django.forms import forms, ModelForm, TextInput
from django.contrib.auth.models import User
from django.db import models


class AddPictureForm(ModelForm):
    class Meta:
        model = Picture
        fields = [ 'gallery_pic', 'description', 'author']

        widgets = {
            'description': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок картинки'
            })
        }
