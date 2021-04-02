from django.shortcuts import render
from rest_framework import generics, permissions
# Create your views here.
from rest_framework.exceptions import ValidationError

from crud.models import Post, Comment, Vote
from crud.serializers import (PostSerializer,
                              CreatePostSerializer,
                              CommentSerializer, VoteSerializer)


class CommentCreateView(generics.CreateAPIView):
    """Create review"""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]


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
        serializer.save(voter=self.request.user, post=Post.objects.get(pk=self.kwargs['pk']))