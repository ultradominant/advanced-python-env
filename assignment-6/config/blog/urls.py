from django.urls import path
from . import views

urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view()),
    path('posts_html/', post_list, name='post_list'),
    path('posts_html/<int:pk>/', post_detail, name='post_detail'),
]
