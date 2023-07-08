from django.contrib import admin
from message.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("message", "date_posted", "author")
    fields = ("author", "date_posted", "message")
    readonly_fields = ("date_posted",)
