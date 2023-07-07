from django import forms


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=50)
    body = forms.CharField(max_length=1000, widget=forms.Textarea)