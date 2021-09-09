from news.models import NewsModel, CategoryModel, CommentModel
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, DestroyAPIView
from news.serializers import NewsSerializer, CategorySerializer, CommentSerializer


class NewsCreateView(CreateAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer



class NewsUpdateView(UpdateAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer
    lookup_field = 'slug'



class NewsListView(ListAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer



class NewsDeleteView(DestroyAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer
    lookup_field = 'slug'



class CategoryCreateView(CreateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer



class CategoryUpdateView(UpdateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'



class CategoryListView(ListAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer



class CategoryDeleteView(DestroyAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'



class CommentCreateView(CreateAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer



class CommentUpdateView(UpdateAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'id'



class CommentListView(ListAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer



class CommentDeleteView(DestroyAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'id'