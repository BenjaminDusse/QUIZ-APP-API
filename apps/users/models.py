from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.models import Profile
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    first_name = None
    last_name = None

    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='user', null=True)

