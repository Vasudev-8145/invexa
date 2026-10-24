from django.db import models


from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    phone = models.CharField(max_length=200,unique=True)

    ROLE_CHOICES = (
        ("admin","admin"),
        ("user","user")
    )

    role = models.CharField(max_length=200,choices=ROLE_CHOICES,default="user")