from django.contrib import admin

from app_users.models import UserProfileModel

@admin.register(UserProfileModel)
class UserProfileModelAdmin(admin.ModelAdmin):
    list_display = ['user','image']
    search_fields = ['user']
    list_filter = ['user']
