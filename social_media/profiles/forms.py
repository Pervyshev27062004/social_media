from django.contrib.auth.models import User

from django import forms
from profiles.models import Profile
from django.forms import ModelForm


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField()
    password = forms.CharField(min_length=8, widget=forms.PasswordInput())
    age = forms.IntegerField(min_value=18, max_value=30, required=False)


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=50)
    body = forms.CharField(max_length=1000, widget=forms.Textarea)


class UserUpdateForm(ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User

        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile

        fields = ['profile_pic']
