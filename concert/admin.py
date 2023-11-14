from django.contrib import admin

# Register your models here.
from .models import Concert

admin.site.Register(Concert)
