from django.contrib import admin
from .models import ImageFile,Comment

# Register your models here.

admin.site.register(ImageFile)
admin.site.register(Comment)