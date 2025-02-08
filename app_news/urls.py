from django.urls import path


from app_news import views

app_name = 'news'

urlpatterns = [
    path('all/',views.NewsListView.as_view(),name='list'),
    path('new/<int:pk>',views.NewsDetailView.as_view(),name='detail'),
]