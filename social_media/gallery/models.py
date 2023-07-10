from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Picture(models.Model):
    gallery_pic = models.ImageField(upload_to="pictures")
    description = models.CharField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

