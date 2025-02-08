from django.urls import path

from app_pages import views


app_name = 'pages'

urlpatterns = [
    path('contact/',views.ContactTemplateView.as_view(),name='contact'),
    path('about/',views.AboutTemplateView.as_view(),name='about'),
    path('',views.HomeTemplateView.as_view(),name='home')
]