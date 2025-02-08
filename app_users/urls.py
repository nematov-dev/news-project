from django.urls import path
from django.contrib.auth.views import LogoutView

from app_users import views

app_name = 'users'

urlpatterns = [
    path('register/',views.RegisterView.as_view(),name='register'),
    path('login/',views.LoginFormView.as_view(),name='login'),
    path('logout/',views.user_logout,name='logout'),
    path("verification/page/", views.EmailVerificationView.as_view(), name="verification-page"),
    path("verification/<int:uid>/<str:token>/", views.VerificationView.as_view(), name="verification"),
    path("my/account/",views.DashboardTemplateView.as_view(),name='account'),
    path('change-password/',views.ChangePasswordView.as_view(),name='change-password'),
    path('profile/edit/', views.ProfileEditView.as_view(), name='profile-edit'),
    
]