from django.shortcuts import render
from gallery.models import Picture
from django.views.generic import ListView, DetailView


class PictureListView(ListView):
    model = Picture
    template_name = 'gallery.html'
    context_object_name = 'pictures'
    paginate_by = 10


class PictureDetailView(DetailView):
    model = Picture
    template_name = "picture_detail.html"
