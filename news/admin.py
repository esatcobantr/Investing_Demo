from django.contrib import admin
from news.models import CategoryModel, NewsModel


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title',)

@admin.register(NewsModel)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_time', 'updated_time')
    search_fields = ('title', 'content')
