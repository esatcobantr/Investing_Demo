from rest_framework import serializers
from news.models import NewsModel, CategoryModel, CommentModel



class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsModel
        fields = ['slug', 'user', 'title', 'content', 'category']



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['slug', 'title']



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = ['comment', 'user', 'content']