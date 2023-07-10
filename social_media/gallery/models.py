from django.db import models
from django.contrib.auth.models import User


class Picture(models.Model):
    gallery_pic = models.ImageField(upload_to="pictures")
    description = models.CharField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

