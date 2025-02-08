from django.urls import path


from app_blogs import views

app_name = "blogs"

urlpatterns = [
    path('all/',views.BlogListView.as_view(),name='list'),
    path('blog/<int:pk>',views.BlogDetailView.as_view(),name='detail'),
]