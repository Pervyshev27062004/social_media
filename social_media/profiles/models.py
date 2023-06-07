from django.conf import settings
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True
    )


class Post(models.Model):
    title = models.CharField(max_length=200)
    profile = models.ForeignKey(
        'profiles.Profile', on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    body = models.TextField()

    def __str__(self):
        return self.title
