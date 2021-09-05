from django.urls import path
from news.views import NewsCreateView, NewsUpdateView, NewsListView, NewsDeleteView, CategoryCreateView, CategoryUpdateView, CategoryListView, CategoryDeleteView

urlpatterns = [
    path('news_create/', NewsCreateView.as_view(), name='news_create'),
    path('news_update/<slug>', NewsUpdateView.as_view(), name='news_update'),
    path('news_list/', NewsListView.as_view(), name='news_list'),
    path('news_delete/<slug>', NewsDeleteView.as_view(), name='news_delete'),
    path('category_create/', CategoryCreateView.as_view(), name='category_create'),
    path('category_update/<slug>', CategoryUpdateView.as_view(), name='category_update'),
    path('category_list/', CategoryListView.as_view(), name='category_list'),
    path('category_delete/<slug>', CategoryDeleteView.as_view(), name='category_delete'),
]