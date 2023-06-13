from django.contrib import admin

from profiles.models import Profile
from profiles.models import Note


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "first_name", "profile_pic", "last_name", "age", "created_at")
    fields = ("user", "profile_pic", "first_name", "last_name", "age", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("first_name", "last_name")


@admin.register(Note)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "profile", "created_at", "body")
    fields = ("title", "profile", "created_at")
    readonly_fields = ("created_at",)

