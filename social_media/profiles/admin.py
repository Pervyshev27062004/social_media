from django.contrib import admin

from profiles.models import Profile
from profiles.models import Post


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "first_name", "last_name", "created_at")
    fields = ("user", "first_name", "last_name", "age", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("first_name", "last_name")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "profile", "created_at")
    fields = ("title", "profile", "created_at")
    readonly_fields = ("created_at",)

