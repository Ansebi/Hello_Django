from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    AuthorPostListView
)

urlpatterns = [
    # path('', views.home, name='hello_app-home'),
    path('', PostListView.as_view(), name='hello_app-home'),
    path('user/<str:username>', AuthorPostListView.as_view(), name='author-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('charts/', views.charts, name='charts'),
    path('circles/', views.circles, name='circles')
]
