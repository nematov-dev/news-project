from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from app_users.models import UserProfileModel

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfileModel.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()