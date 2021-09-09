from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User


class CategoryModel(models.Model):
    title = models.CharField(max_length = 30, blank = False, null = False)
    slug = AutoSlugField(populate_from = 'title', null = True, unique = True)

    class Meta:
        db_table = 'Category'
        verbose_name_plural = 'Category'
        verbose_name = 'Categories'

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
    category = models.ManyToManyField(CategoryModel, related_name = 'newscategory')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='newsuser')

    class Meta:
        db_table = 'News'
        verbose_name_plural = 'News'
        verbose_name = 'News'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = (self.title)
        return super(NewsModel, self).save(*args, **kwargs)

    

class CommentModel(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commentuser')
    content = models.ForeignKey(NewsModel, on_delete=models.CASCADE, related_name='commentcontent')        
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    created_time = models.DateTimeField(auto_now_add = True)
    updated_time = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'Comment'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.content.title + " " + self.user.username

    def child(self):
        return CommentModel.objects.filter(parent=self)

    @property
    def any_child(self):
        return CommentModel.objects.filter(parent=self).exists()