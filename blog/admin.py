from django.contrib import admin

# Register your models here.
# Registrar modelos en esta parte
from django.contrib import admin
from .models import Post

admin.site.register(Post)