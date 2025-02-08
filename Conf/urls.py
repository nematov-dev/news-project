from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include('app_users.urls',namespace='users')),
    path('news/',include('app_news.urls',namespace='news')),
    path('blogs/',include('app_blogs.urls',namespace='blogs')),
    path('',include('app_pages.urls',namespace='pages')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)