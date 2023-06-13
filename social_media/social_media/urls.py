from django.contrib import admin
from django.urls import path
from django.conf import settings


from profiles.views import register, login_view, my_page, ShowProfilePageView, CreateProfilePageView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", register, name="register"),
    path("login/", login_view, name="login"),
    path("my_page/", my_page, name="my_page"),
    path("user_profile/<int:pk>/", ShowProfilePageView.as_view(), name='user_profile'),
    path('create_profile_page/', CreateProfilePageView.as_view(), name='create_profile'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

