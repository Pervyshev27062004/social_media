from django import forms


class AddMessageForm(forms.Form):
    title = forms.CharField(max_length=50)
    message = forms.CharField(max_length=1000, widget=forms.Textarea)