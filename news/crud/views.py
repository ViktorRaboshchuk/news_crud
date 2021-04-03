from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, permissions, status

# Create your views here.
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from crud.models import Post, Comment, Vote
from crud.serializers import (
    PostSerializer,
    CreatePostSerializer,
    CommentSerializer,
    VoteSerializer,
    CreateCommentSerializer,
)


class CommentCreateView(generics.CreateAPIView):
    """Create review"""

    queryset = Comment.objects.all()
    serializer_class = CreateCommentSerializer
    # permission_classes = [permissions.IsAuthenticated]


class CommentListView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = [permissions.IsAuthenticated]


class PostCreateView(generics.ListCreateAPIView):
    """Create review"""

    queryset = Post.objects.all()
    serializer_class = CreatePostSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all()
    serializer_class = CreatePostSerializer
    permission_classes = [permissions.IsAuthenticated]


class VoteCreateView(generics.CreateAPIView):
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        post = Post.objects.get(pk=self.kwargs["pk"])
        vote_obj = Vote.objects.filter(voter=user, post=post)
        return vote_obj

    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError("Already upvoted!")
        serializer.save(
            voter=self.request.user, post=Post.objects.get(pk=self.kwargs["pk"])
        )


class VotesDeleteView(generics.DestroyAPIView):

    def delete(self, *args, **kwargs):
        votes = Vote.objects.all()
        votes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
