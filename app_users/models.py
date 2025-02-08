from django.db import models
from django.contrib.auth.models import User

class UserProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    image = models.ImageField(upload_to='profile_pics/', default='profile_pics/user.jpg')

    def __str__(self):
        return f"{self.user.username} profili"
    
    class Meta:
        verbose_name = 'Profil'
        verbose_name_plural = 'Profillar'
