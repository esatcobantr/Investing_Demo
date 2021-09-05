from django.urls import path
from news.views import (
    NewsCreateView, NewsUpdateView, NewsListView, NewsDeleteView, 
    CategoryCreateView, CategoryUpdateView, CategoryListView, CategoryDeleteView,
    CommentCreateView, CommentUpdateView, CommentListView, CommentDeleteView
    )

urlpatterns = [
    path('news_create/', NewsCreateView.as_view(), name='news_create'),
    path('news_update/<slug>', NewsUpdateView.as_view(), name='news_update'),
    path('news_list/', NewsListView.as_view(), name='news_list'),
    path('news_delete/<slug>', NewsDeleteView.as_view(), name='news_delete'),
    path('category_create/', CategoryCreateView.as_view(), name='category_create'),
    path('category_update/<slug>', CategoryUpdateView.as_view(), name='category_update'),
    path('category_list/', CategoryListView.as_view(), name='category_list'),
    path('category_delete/<slug>', CategoryDeleteView.as_view(), name='category_delete'),
    path('comment_create/', CommentCreateView.as_view(), name='comment_create'),
    path('comment_update/<id>', CommentUpdateView.as_view(), name='comment_update'),
    path('comment_list/', CommentListView.as_view(), name='comment_list'),
    path('comment_delete/<id>', CommentDeleteView.as_view(), name='comment_delete'),
]