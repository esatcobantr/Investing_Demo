from news.models import NewsModel, CategoryModel
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, DestroyAPIView
from news.serializers import NewsCreateSerializer, NewsUpdateSerializer, NewsListSerializer, NewsDeleteSerializer, CategoryCreateSerializer, CategoryUpdateSerializer, CategoryListSerializer, CategoryDeleteSerializer


class NewsCreateView(CreateAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsCreateSerializer



class NewsUpdateView(UpdateAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsUpdateSerializer
    lookup_field = 'slug'



class NewsListView(ListAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsListSerializer



class NewsDeleteView(DestroyAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsDeleteSerializer
    lookup_field = 'slug'



class CategoryCreateView(CreateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategoryCreateSerializer



class CategoryUpdateView(UpdateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategoryUpdateSerializer
    lookup_field = 'slug'



class CategoryListView(ListAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategoryListSerializer



class CategoryDeleteView(DestroyAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategoryDeleteSerializer
    lookup_field = 'slug'
