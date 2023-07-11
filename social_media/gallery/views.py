from django.shortcuts import render, redirect
from gallery.models import Picture
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from gallery.forms import AddPictureForm
from django.contrib.auth.models import User


class PictureListView(ListView):
    model = Picture
    template_name = 'gallery_all.html'
    context_object_name = 'pictures'
    paginate_by = 10


class PictureDetailView(DetailView):
    model = Picture
    template_name = "picture_detail.html"


class UserPictureListView(ListView):
    model = Picture
    template_name = 'user_pictures.html'
    context_object_name = 'pictures'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Picture.objects.filter(author=user).order_by('-date_posted')


def post_picture(request):
    error = ''
    if request.method == "POST":
        form = AddPictureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gallery_all')
        else:
            error = 'Форма была неверной'
    form = AddPictureForm()

# data is a dictionary
    data = {
        'form': form,
        'error': error
    }
    return render(request, "add_picture.html", data)