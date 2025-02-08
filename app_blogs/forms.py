from django import forms


from app_blogs import models

class BlogsCommentForm(forms.ModelForm):
    class Meta:
        model = models.BlogCommentModel
        fields = ('comment',)
