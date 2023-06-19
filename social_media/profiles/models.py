from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default.jpg', upload_to='profile_pics')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(default=21)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)


def __str__(self):
    return str(self.user)


class Note(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'profiles.Profile',
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    body = models.TextField()

    def __str__(self):
        return self.title
