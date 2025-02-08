from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

from app_common.models import BaseModel


User = get_user_model()

class PublishedManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(status=NewsModel.Status.Published)

class NewsCategoryModel(BaseModel):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "News Category"
        verbose_name_plural = "News Categories"

class NewsTagModel(BaseModel):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "News title"
        verbose_name_plural = "News titles"
    

class NewsAuthorModel(BaseModel):
    first_name = models.CharField(max_length=128, verbose_name=('first_name'))
    last_name = models.CharField(max_length=128, verbose_name=('last_name'))
   
    @property
    def full_name(self):
        return self.__repr__()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'News author'
        verbose_name_plural = 'News authors'

class NewsModel(BaseModel):

    class Status(models.TextChoices):
        Draft = "DF","Draft"
        Published = "PB","Published"

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='news')
    publish_time = models.DateField(default=timezone.now)
    status = models.CharField(max_length=2,choices=Status.choices,default=Status.Draft)

    authors = models.ManyToManyField(
        NewsAuthorModel,
        related_name="news"
    )

    categories = models.ManyToManyField(
        NewsCategoryModel,
        related_name="news"
    )

    tags = models.ManyToManyField(
        NewsTagModel,
        related_name="news"
    )

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-publish_time"]
        verbose_name = "New"
        verbose_name_plural = "News"
    
class NewsCommentModel(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="users")
    
    news = models.ForeignKey(
        NewsModel,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    message = models.TextField()

    def __str__(self):
        return f"{self.user.username} → {self.news.title}"
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
    

