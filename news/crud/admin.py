from django.contrib import admin

from crud.models import Post, Comment, Vote

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Vote)
