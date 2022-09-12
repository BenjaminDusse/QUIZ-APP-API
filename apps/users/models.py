from django.db import models
from django.contrib.auth.models import AbstractUser

from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    username = None
    first_name = None
    last_name = None
    email = None

    contact = models.OneToOneField('contact.Contact', on_delete=models.CASCADE, related_name='user')

