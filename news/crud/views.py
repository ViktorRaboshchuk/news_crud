"""A view function, or view for short,
is a Python function that takes a Web request and returns a Web response"""
from rest_framework import generics, permissions, status

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
    """Create a new comment instance"""

    queryset = Comment.objects.all()
    serializer_class = CreateCommentSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentListView(generics.ListAPIView):
    """List all comment instances"""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete a comment instance"""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostCreateView(generics.ListCreateAPIView):
    """Create a new post instance"""

    queryset = Post.objects.all()
    serializer_class = CreatePostSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostListView(generics.ListAPIView):
    """List all posts instances"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete a post instance"""

    queryset = Post.objects.all()
    serializer_class = CreatePostSerializer
    permission_classes = [permissions.IsAuthenticated]


class VoteCreateView(generics.CreateAPIView):
    """Create a new vote instance"""

    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Get all vote instances for specific user ID"""
        user = self.request.user
        post = Post.objects.get(pk=self.kwargs["pk"])
        vote_obj = Vote.objects.filter(voter=user, post=post)
        return vote_obj

    def perform_create(self, serializer):
        """Check if user upvoted particular post, if not saves vote instance"""
        if self.get_queryset().exists():
            raise ValidationError("Already upvoted!")
        serializer.save(
            voter=self.request.user,
            post=Post.objects.get(pk=self.kwargs["pk"]),
        )


class VotesDeleteView(generics.DestroyAPIView):
    """Deleting all votes"""

    def delete(self, *args, **kwargs):
        votes = Vote.objects.all()
        print("votes: ", votes)
        votes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
