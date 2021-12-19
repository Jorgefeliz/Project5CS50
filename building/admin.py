from django.contrib import admin

# Register your models here.
from .models import User, Events, Profile, Announcement, Issues

admin.site.register(User)
admin.site.register(Events)
admin.site.register(Profile)
admin.site.register(Announcement)
admin.site.register(Issues)
