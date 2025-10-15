from django.urls import path
from .views import PostList, PostDetail, create_product

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('create/', create_product, name='post_create'),
]