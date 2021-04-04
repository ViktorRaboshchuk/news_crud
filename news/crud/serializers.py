"""
Serializers allow complex data such as querysets and model instances
to be converted to native Python datatypes,
that can then be easily rendered into JSON, XML or other content types.
"""
from django.contrib.auth.models import User
from rest_framework import serializers

from crud.models import Post, Comment, Vote


class UserSerializer(serializers.ModelSerializer):
    # """Serializes User data"""
    class Meta:
        model = User
        fields = (
            "id",
            "username",
        )


class CommentSerializer(serializers.ModelSerializer):
    """Serializes all comments"""

    class Meta:
        model = Comment
        fields = ("id", "content", "creation_date")


class CreateCommentSerializer(serializers.ModelSerializer):
    """Serializes fields for new comments"""

    class Meta:
        model = Comment
        fields = ("id", "post", "author", "content", "creation_date")


class PostSerializer(serializers.ModelSerializer):
    """Serializes fields for post data"""

    comments = CommentSerializer(many=True)
    author = UserSerializer()
    votes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "creation_date",
            "author",
            "votes",
            "comments",
        )

    def get_votes(self, post):
        """Count all votes for each post"""
        return Vote.objects.filter(post=post).count()


class CreatePostSerializer(serializers.ModelSerializer):
    """Serializes fields for new post"""

    class Meta:
        model = Post
        fields = "__all__"


class VoteSerializer(serializers.ModelSerializer):
    """Serializes id field after vote action"""

    class Meta:
        model = Vote
        fields = ("id",)
