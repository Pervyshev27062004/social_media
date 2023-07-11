from gallery.models import Picture
from django.forms import ModelForm


class LookGalleryForm(ModelForm):
    class Meta:
        model = Picture
        fields = [ 'author']
