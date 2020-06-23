from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'admin'),
        (2, 'employee'),
        (3, 'customer')
    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
# Create your models here.
