from django.contrib import admin
from gallery.models import Picture


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ("gallery_pic", "description", "author")
    fields = ("gallery_pic", "description", "author")