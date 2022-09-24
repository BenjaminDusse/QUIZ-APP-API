from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """ User Table to store user information """
    
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200)
    intro = models.TextField(help_text="The brief introduction of the Host User to be displayed on the Test or Quiz Page", max_length=300, blank=True)

