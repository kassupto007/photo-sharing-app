from django.conf import settings
from django.db import models
from django.utils import timezone
from users.models import Profile


class Post(models.Model):
    description = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='posts', blank=True)
    date_posted = models.DateTimeField(auto_now_add=True, auto_now=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    comment_date = models.DateTimeField(auto_now_add=True, auto_now=False)
