from django.contrib import admin
from django.urls import path

from profiles.views import register, login_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", register, name="register"),
    path("login/", login_view, name="login"),
]
