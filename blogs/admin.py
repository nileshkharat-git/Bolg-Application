from django.contrib import admin
from .models import Blogs

class BlogAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'article']

admin.site.register(Blogs,BlogAdmin)