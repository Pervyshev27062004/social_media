from django.contrib.auth.models import User

from django import forms
from profiles.models import Profile, Post
from django.forms import ModelForm, TextInput, Textarea


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField()
    password = forms.CharField(min_length=8, widget=forms.PasswordInput())
    age = forms.IntegerField(min_value=18, max_value=30, required=False)


class AddPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название поста'
            }),
            "content": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Текст поста"
            }),
        }


class UserUpdateForm(ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User

        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile

        fields = ['profile_pic']
