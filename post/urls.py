from django.urls import path

from post.views import PostListView, UpdatePostView

urlpatterns = [
    path('create/', PostListView.as_view(), name='create_post'),
    path('update/<int:pk>/', UpdatePostView.as_view(), name='update_post')
]
