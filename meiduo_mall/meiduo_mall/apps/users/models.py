from django.db import models

from django.contrib.auth.models import User, AbstractUser

# Create your models here.

class User(AbstractUser):
    mobile = models.CharField(max_length=11)