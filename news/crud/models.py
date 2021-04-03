from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=150)
    link = models.URLField(max_length=600, default="")
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User, related_name="post_author_name", on_delete=models.CASCADE
    )


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(
        User, related_name="comment_author_name", on_delete=models.CASCADE
    )
    content = models.TextField(max_length=400, blank=False)
    creation_date = models.DateTimeField(auto_now_add=True)


class Vote(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
