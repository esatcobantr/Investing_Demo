from news.models import NewsModel, CategoryModel, CommentModel
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListAPIView, RetrieveDestroyAPIView
from news.serializers import NewsSerializer, CategorySerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from news.permissions import IsSuperOrAuthorUser, IsSuperUser
from rest_framework.filters import SearchFilter, OrderingFilter


class NewsCreateView(CreateAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)


class NewsUpdateView(RetrieveUpdateAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer
    lookup_field = 'slug'
    permission_classes = [IsSuperOrAuthorUser]



class NewsListView(ListAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['user', 'slug', 'title', 'content', 'category']



class NewsDeleteView(RetrieveDestroyAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer
    lookup_field = 'slug'
    permission_classes = [IsSuperOrAuthorUser]



class CategoryCreateView(CreateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsSuperUser]

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)



class CategoryUpdateView(RetrieveUpdateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    permission_classes = [IsSuperUser]



class CategoryListView(ListAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['user', 'slug', 'title']



class CategoryDeleteView(RetrieveDestroyAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    permission_classes = [IsSuperUser]



class CommentCreateView(CreateAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)



class CommentUpdateView(RetrieveUpdateAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'id'
    permission_classes = [IsSuperOrAuthorUser]



class CommentListView(ListAPIView):
    serializer_class = CommentSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['id', 'user', 'comment', 'content', 'parent']

    def get_queryset(self):
        return CommentModel.objects.filter(parent = None)



class CommentDeleteView(RetrieveDestroyAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'id'
    permission_classes = [IsSuperOrAuthorUser]