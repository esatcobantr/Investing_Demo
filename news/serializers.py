from rest_framework import serializers
from news.models import CategoryModel, NewsModel, CommentModel


class NewsSerializer(serializers.ModelSerializer):

    username = serializers.SerializerMethodField()

    class Meta:
        model = NewsModel
        fields = ['username', 'slug', 'title', 'content', 'category', 'image']

    def get_username(self, obj):
        return str(obj.user.username)


class CategorySerializer(serializers.ModelSerializer):

    username = serializers.SerializerMethodField()

    class Meta:
        model = CategoryModel
        fields = ['username', 'slug', 'title']

    def get_username(self, obj):
        return str(obj.user.username)


class CommentSerializer(serializers.ModelSerializer):

    username = serializers.SerializerMethodField()
    contentname = serializers.SerializerMethodField()
    replies = serializers.SerializerMethodField()

    class Meta:
        model = CommentModel
        fields = ['id', 'username', 'comment', 'content',
                  'contentname', 'parent', 'replies']

    def validate(self, attrs):
        if(attrs['parent']):
            if attrs['parent'].content != attrs['content']:
                raise serializers.ValidationError("Something went wrong!")
        return attrs

    def get_username(self, obj):
        return str(obj.user.username)

    def get_contentname(self, obj):
        return str(obj.content.title)

    def get_replies(self, obj):
        if obj.any_child:
            return CommentSerializer(obj.child(), many=True).data
