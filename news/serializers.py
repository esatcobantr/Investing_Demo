from rest_framework import serializers
from news.models import NewsModel, CategoryModel



class NewsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsModel
        fields = ['title', 'content', 'category']



class NewsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsModel
        fields = ['title', 'content']



class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsModel
        fields = ['slug', 'title', 'content', 'category']



class NewsDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsModel
        fields = ['title', 'content']



class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['slug', 'title']



class CategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['slug', 'title']


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['slug', 'title']


    
class CategoryDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['slug', 'title']