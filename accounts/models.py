from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    following = models.ManyToManyField('self', symmetrical=False, related_name='follower')
    # follower = 라는 컬럼이 자동으로 생김

