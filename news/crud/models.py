"""
A model is the single, definitive source of information about your data.
It contains the essential fields and behaviors of the data you’re storing.
Generally, each model maps to a single database table.
"""
from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    """Model for objects"""

    title = models.CharField(max_length=150)
    link = models.URLField(max_length=600, default="")
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User, related_name="post_author_name", on_delete=models.CASCADE
    )


class Comment(models.Model):
    """Model for Comment objects"""

    post = models.ForeignKey(
        Post, related_name="comments", on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        User, related_name="comment_author_name", on_delete=models.CASCADE
    )
    content = models.TextField(max_length=400, blank=False)
    creation_date = models.DateTimeField(auto_now_add=True)


class Vote(models.Model):
    """Model for Vote objects"""

    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
