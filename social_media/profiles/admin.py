from django.contrib import admin
from profiles.models import Profile
from profiles.models import Post


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "first_name",
        "profile_pic",
        "last_name",
        "age",
        "created_at",
    )
    fields = ("user", "profile_pic", "first_name", "last_name", "age", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("first_name", "last_name")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "date_posted", "author")
    fields = ("title", "author", "date_posted", "content")
    readonly_fields = ("date_posted",)
