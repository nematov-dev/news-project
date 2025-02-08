from django import forms


from app_news import models

class NewsCommentForm(forms.ModelForm):
    class Meta:
        model = models.NewsCommentModel
        fields = ('message',)

