from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Message(models.Model):
    message = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)