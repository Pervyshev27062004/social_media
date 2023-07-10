from django.shortcuts import render
from gallery.models import Picture
from django.views.generic import ListView


class PictureListView(ListView):
    model = Picture
    template_name = 'gallery.html'
    context_object_name = 'pictures'
    paginate_by = 10
