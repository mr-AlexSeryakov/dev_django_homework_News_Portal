from django.urls import path
from .views import (
    PostList, PostDetail, NewsCreateView, ArticleCreateView, NewsUpdate, ArticleUpdate, NewsDelete, ArticleDelete, NewsSearchView,
)

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    #
    path('create/', NewsCreateView.as_view(), name='news_create'),
    path('articles/create/', ArticleCreateView.as_view(), name='articles_create'),
    #
    path('<int:pk>/edit/', NewsUpdate.as_view(), name='post_update'),
    path('articles/<int:pk>/edit/', ArticleUpdate.as_view(), name='article_update'),
    #
    path('<int:pk>/delete/', NewsDelete.as_view(), name='post_delete'),
    path('articles/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
    #
    path('search/', NewsSearchView.as_view(), name='news_search'),

]