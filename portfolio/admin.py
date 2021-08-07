from django.contrib import admin
from .models import Project
admin.site.register(Project)
from blog.models import all_blogs1
admin.site.register(all_blogs1)