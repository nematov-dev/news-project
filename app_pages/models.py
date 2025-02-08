from django.db import models


from app_common.models import BaseModel

class AboutModel(BaseModel):
    fullname = models.CharField(max_length=128)
    job = models.CharField(max_length=255)
    image = models.ImageField(upload_to='team')

    def __str__(self) -> str:
        return self.fullname
    
    class Meta:
        verbose_name = "Worker"
        verbose_name_plural = "Workers"


class ContactModel(BaseModel):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"




