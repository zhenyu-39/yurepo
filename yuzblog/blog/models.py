from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import CharField

User = get_user_model()

# Create your models here.
class BlogCategory(models.Model):
    name = models.CharField(max_length=200,verbose_name='分类名称')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

class Blog(models.Model):
    title = models.CharField(max_length=200,verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    pub_time = models.DateTimeField(auto_now_add=True,verbose_name='发布时间')
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE,verbose_name='分类')
    author = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='作者')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name
        ordering = ['-pub_time']

class BlogComment(models.Model):
    content = models.TextField(verbose_name='内容')
    pub_time = models.DateTimeField(auto_now_add=True,verbose_name='发布时间')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE,related_name='comments',verbose_name='所属博客')
    author = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='作者')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        ordering = ['-pub_time']

class BlogImage(models.Model):
    content = models.TextField(verbose_name='内容')
    pub_time = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='images', verbose_name='所属博客', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='留言人')

    class Meta:
        verbose_name = '留言'
        verbose_name_plural = verbose_name
        ordering = ['-pub_time']