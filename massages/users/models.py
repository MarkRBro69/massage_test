from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    home_page = models.URLField(null=True, blank=True)
