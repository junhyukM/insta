from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField
from posts.models import Post
from django.conf import settings
# Create your models here.

class User(AbstractUser):
    following = models.ManyToManyField('self', symmetrical=False, related_name='follower')
    # follower = 라는 컬럼이 자동으로 생김
    # profile_image = models.ImageField(upload_to='profiles')

    profile_image = ResizedImageField(
        size=[500, 500],
        crop=['middle', 'center'],
        upload_to = 'profiles',
    )
    bookmarks = models.ManyToManyField(
        Post,
        through='Bookmark',
        related_name='bookmark_users',
    )

class Bookmark(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)