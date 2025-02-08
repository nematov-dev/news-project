from django.contrib import admin
from app_blogs import models

from django.contrib import admin

# from app_common.admin import MyTranslationAdmin
from .models import BlogCategoryModel, BlogTagModel, BlogAuthorModel, BlogModel, BlogCommentModel


@admin.register(BlogCategoryModel)
class BlogCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title',]
    search_fields = ['title',]
    list_filter = ['title',]


@admin.register(BlogTagModel)
class BlogTagModelAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


@admin.register(BlogAuthorModel)
class BlogAuthorModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'avatar']
    search_fields = ['first_name', 'last_name']


@admin.register(BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'get_author_names']
    search_fields = ['title', 'description']
    filter_horizontal = ['authors', 'categories']

    def get_author_names(self, obj):
        return ", ".join([author.full_name for author in obj.authors.all()])

    get_author_names.short_description = 'Authors'


@admin.register(BlogCommentModel)
class BlogCommentModelAdmin(admin.ModelAdmin):
    list_display = ['comment', 'user', 'created_at']
    search_fields = ['comment']
    list_filter = ['user']