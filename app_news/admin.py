from django.contrib import admin

from app_news import models

@admin.register(models.NewsModel)
class NewsModelAdmin(admin.ModelAdmin):
    list_display = ('title','publish_time','status')
    search_fields = ('title','body')
    list_filter = ('status','created_at','publish_time')
    prepopulated_fields = {"slug":("title",)}
    date_hierarchy = 'publish_time'
    ordering = ('status','publish_time')


@admin.register(models.NewsCategoryModel)
class NewsCategoryModelAdmin(admin.ModelAdmin):
    list_display = ('title','created_at')
    search_fields = ('title',)
    list_filter = ('created_at',)

@admin.register(models.NewsTagModel)
class NewsTagModelAdmin(admin.ModelAdmin):
    list_display = ('title','created_at')
    search_fields = ('title',)
    list_filter = ('created_at',)

@admin.register(models.NewsAuthorModel)
class NewsCategoryModelAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','created_at')
    search_fields = ('first_name','last_name',)
    list_filter = ('created_at',)

@admin.register(models.NewsCommentModel)
class NewsCommentModelAdmin(admin.ModelAdmin):
    list_display = ('message','created_at')
    search_fields = ('message',)
    list_filter = ('created_at',)



