from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.contrib.auth import views as auth_views
from profiles import views as user_views
from message.views import MessageListView, post_message


from profiles.views import (
    register,
    ShowProfilePageView,
    CreateProfilePageView,
    post,
    PostListView,
    PostDetailView,
    PostDeleteView,
    UserPostListView,
)

urlpatterns = [
    path("", PostListView.as_view(), name="home"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("user/<str:username>", UserPostListView.as_view(), name="user-posts"),
    path("admin/", admin.site.urls),
    path("register/", register, name="register"),
    path(
        "login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="logout.html"),
        name="logout",
    ),
    path("profile/", user_views.profile, name="profile"),
    path("user_profile/<int:pk>/", ShowProfilePageView.as_view(), name="user_profile"),
    path(
        "create_profile_page/", CreateProfilePageView.as_view(), name="create_profile"
    ),
    path("add_post", post, name="add_post"),
    path("messages/", MessageListView.as_view(), name="message"),
    path("add_message/", post_message, name="add_message"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
