from django.contrib.auth.models import User
from rest_framework import serializers

from crud.models import Post, Comment, Vote


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


class CommentSerializer(serializers.ModelSerializer):
    """ Add review """

    author = UserSerializer()

    class Meta:
        model = Comment
        fields = ("id", "author", "content", "creation_date")


class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("post", "author", "content", "creation_date")


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    author = UserSerializer()
    votes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ("id", "title", "creation_date", "author", "votes", "comments")

    def get_votes(self, post):
        return Vote.objects.filter(post=post).count()


class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ("id",)
