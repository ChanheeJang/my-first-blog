from django.contrib import admin
from .models import Post

admin.site.register(Post)  

##--!!(6)만든거 추가 후 --> python manage.py createsuperuser