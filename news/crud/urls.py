from django.urls import path

from crud import views

urlpatterns = [
    path('post/<int:pk>/', views.PostRetrieveUpdateDestroyView.as_view()),
    path('comment/<int:pk>/', views.CommentRetrieveUpdateDestroyView.as_view()),

    path('new_post/', views.PostCreateView.as_view()),
    path('new_comment/', views.CommentCreateView.as_view()),

    path('posts/', views.PostListView.as_view()),

    path('post/<int:pk>/vote/', views.VoteCreateView.as_view()),
]
