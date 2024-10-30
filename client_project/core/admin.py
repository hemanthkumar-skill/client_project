from django.contrib import admin
from .models import Client, Project

# Register Client and Project models
admin.site.register(Client)
admin.site.register(Project)
