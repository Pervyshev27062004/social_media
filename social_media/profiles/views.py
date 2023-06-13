import logging
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from profiles.forms import RegisterForm, LoginForm, AddNoteForm

from profiles.models import Profile, Note

logger = logging.getLogger(__name__)

posts = [
    {
        'author': 'Администратор',
        'title': 'Это первый пост',
        'content': 'Содержание первого поста.',
        'date_posted': '12 мая, 2022'
    },
    {
        'author': 'Пользователь',
        'title': 'Это второй пост',
        'content': 'Подробное содержание второго поста.',
        'date_posted': '13 мая, 2022'
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'home.html', context)


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User(
                email=form.cleaned_data["email"],
                username=form.cleaned_data["last_name"],
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
            )
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect("create_profile")
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context


class CreateProfilePageView(CreateView):
    model = Profile

    template_name = 'create_profile.html'
    fields = ['profile_pic', 'first_name', 'last_name', 'age']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('login')


@login_required
def profile(request):
    return render(request, 'profile.html')


def post(request):
    notes = Note.objects.all()
    if request.method == "POST":
        form = AddNoteForm(request.POST)
        if form.is_valid():
            Note.objects.create(
                user=request.user,
                title=form.cleaned_data["title"],
                text=form.cleaned_data["body"]
            )
            return redirect("post")
    else:
        form = AddNoteForm()
    return render(request, "index.html", {"notes": notes, "form": form})

