from django.contrib import admin


from app_pages import models


@admin.register(models.AboutModel)
class AboutModelAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'job')  
    search_fields = ('fullname', 'job')
    list_filter = ('fullname','job')

@admin.register(models.ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')  
    search_fields = ('subject', 'message')
    list_filter = ('email','created_at')