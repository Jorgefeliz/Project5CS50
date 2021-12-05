from django.contrib import admin

# Register your models here.
from .models import User, Events, Profile

admin.site.register(User)
admin.site.register(Events)
admin.site.register(Profile)
