from django.contrib import admin
from django.urls import path

from profiles.views import register, login_view, my_page

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", register, name="register"),
    path("login/", login_view, name="login"),
    path("my_page/", my_page, name="my_page"),
]
