from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(User,related_name='blog_author',on_delete=models.CASCADE)
    blog_title = models.CharField(max_length=100,verbose_name='put blog title here')
    blog_content = models.TextField(verbose_name='What\'s on your mind?')
    blog_image = models.ImageField(upload_to='blog_image',verbose_name='Image')
    slug = models.SlugField(max_length=100,unique=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-publish_date',)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User,related_name='user_comment',on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog,related_name='blog_comment',on_delete=models.CASCADE)
    comment = models.TextField(max_length=400)
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
    class Meta:
        ordering = ('-comment_date',)

class Likes(models.Model):
    user = models.ForeignKey(User,related_name='liker_user',on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog,related_name='like_blog',on_delete=models.CASCADE)
    def __init__(self):
        return self.user + "likes "+self.blog
