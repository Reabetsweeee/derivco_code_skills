from django.contrib import admin
from .models import Comment, CollabRequest

admin.site.register(Comment)
admin.site.register(CollabRequest)