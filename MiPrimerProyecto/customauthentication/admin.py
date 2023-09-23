from django.contrib import admin

# Register your models here.
from .models import CustomUserAuthentication
from django.contrib.auth.admin import UserAdmin
from .models import CustomUserAuthentication

admin.site.register(CustomUserAuthentication, UserAdmin)
