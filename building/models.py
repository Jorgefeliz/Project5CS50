from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    pass

    def serialize(self):
        return {
            "id": self.id,
            "user": self.username,
            
        }