from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    """
    Extended user model for Mzansi Builds
    Add a bio and fields on top of the Django's built in user
    """
    bio = models.TextField(blank=True)
    github_url= models.URLField(blank=True)
    google_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    avatar = models.URLField(blank=True)

    def __str__(self):
        return self.username