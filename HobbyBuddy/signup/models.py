from django.db import models
from django.contrib.auth.models import AbstractUser as U


# Create your models here.
class User(U):
    is_premium = models.BooleanField(default=False)

