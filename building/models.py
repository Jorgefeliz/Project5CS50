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

class Profile (models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="residents")
    residencial = models.CharField(max_length=128)
    building = models.CharField(max_length=64)
    apto = models.CharField(max_length=64)
    role = models.CharField(max_length=64, default="resident")

class Events(models.Model):
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="events")
    event_date = models.DateTimeField()
    submited = models.DateTimeField(auto_now_add=True)
    place = models.CharField(max_length=64)
    type_of_event = models.CharField(max_length=64)
    status = models.CharField(max_length=64)

    def serialize(self):
        return {
            "id": self.id,
            "event_date": self.event_date,
            "place": self.place,
            "type_of_event": self.type_of_event,
            "status": self.status
        }


class Announcement(models.Model):
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="announcer")
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=20000, blank=True)
    valid_date = models.DateField()
    submited = models.DateTimeField(auto_now=True)

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "valid_date": self.valid_date,
            "submited": self.submited
        }

class Issues(models.Model):
    title = models.CharField(max_length=255)
    categoria = models.CharField(max_length=128)
    description = models.CharField(max_length=20000)
    status = models.CharField(max_length=96)
    reported_by = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="reporter")
    reported_date = models.DateTimeField(auto_now=True)
    signed_by = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="signer", null=True, blank=True)
    signed_date = models.DateTimeField(null=True, blank=True)

    def serialize(self):
       return {
           "id":self.id,
           "title": self.title,
           "categoria": self.categoria,
           "description": self.description,
           "status": self.status,
           "reported_date": self.reported_date,
           "signed_date": self.signed_date

       }








