from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):
    class Meta:
        db_table = "my_user"
    username = models.CharField(max_length=30, unique=False)
    email = models.EmailField(unique=True)
    user_image = models.CharField(max_length=255, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
