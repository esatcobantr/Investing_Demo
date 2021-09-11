from rest_framework import serializers
from news.models import CategoryModel, NewsModel, CommentModel



class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsModel
        fields = ['user', 'slug', 'title', 'content', 'category', 'image']



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['user', 'slug', 'title']



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = ['id', 'user', 'comment', 'content', 'parent']

    def validate(self, attrs):
        if(attrs['parent']):
            if attrs['parent'].content != attrs['content']:
                raise serializers.ValidationError("Something went wrong!")
        return attrs