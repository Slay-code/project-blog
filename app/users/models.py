from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    status = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'User'
        
    def __str__(self):
        return self.username