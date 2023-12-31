from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django_resized import ResizedImageField

# Create your models here.
class Post(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # image = models.ImageField(upload_to='pic/%m/%d')
    image = ResizedImageField(
        size = [500,500],
        crop = ['middle', 'center'],
        upload_to = 'pic/%m/%d'
    )

    # M 대 N 연결
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')
    # post.like_users.all()
    # user.like_posts.all()


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
