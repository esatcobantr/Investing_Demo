from django.db import models
from autoslug import AutoSlugField


class CategoryModel(models.Model):
    title = models.CharField(max_length = 30, blank = False, null = False)
    slug = AutoSlugField(populate_from = 'title', null = True, unique = True)

    class Meta:
        db_table = 'Category'
        verbose_name_plural = 'Category'
        verbose_name = 'Category'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = (self.title)
        return super(CategoryModel, self).save(*args, **kwargs)



class NewsModel(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add = True)
    updated_time = models.DateTimeField(auto_now = True)
    slug = AutoSlugField(populate_from = 'title', null = True, unique = True)
    category = models.ManyToManyField(CategoryModel, related_name = 'content')

    class Meta:
        db_table = 'News'
        verbose_name_plural = 'News'
        verbose_name = 'News'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = (self.title)
        return super(NewsModel, self).save(*args, **kwargs)