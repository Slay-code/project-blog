from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    status = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'User'
        
    def __str__(self):
        return self.username
    
    def get_absolute_url(self):
        return reverse("users:other_user", args=[self.username])
    