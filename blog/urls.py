from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name="blog_home"),
    path('post/new/', PostCreateView.as_view(), name="post_create"),
    path('user/<str:username>/', UserPostListView.as_view(), name="user_post"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post_update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post_delete"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post_detail"),
    path('about/', views.about, name="blog_about"),
]
