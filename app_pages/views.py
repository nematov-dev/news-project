from typing import Any
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib import messages


from app_pages import models
from app_news.models import NewsModel


class HomeTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs: Any):
        context =  super().get_context_data(**kwargs)
        context['most_recents'] = NewsModel.published.all().order_by('-publish_time')[:6]
       
        context['mahalliy'] = NewsModel.published.filter(categories__title="Mahalliy").order_by('-publish_time').first()
        context['sport'] = NewsModel.published.filter(categories__title="Sport").order_by('-publish_time').first()

        context['uzbekistan_news'] = NewsModel.published.filter(categories__title="O'zbekiston").order_by('-publish_time')[2:6]
        context['uzbekistan_new'] = NewsModel.published.filter(categories__title="O'zbekiston").order_by('-publish_time').first()
        context['uzbekistan_new2'] = NewsModel.published.filter(categories__title="O'zbekiston").order_by('-publish_time')[1]

        context['jahon_news'] = NewsModel.published.filter(categories__title="Jahon").order_by('-publish_time')[:9]

        context['iqtisodiyot_news'] = NewsModel.published.filter(categories__title="Iqtisodiyot").order_by('-publish_time')[:5]

        return context

class AboutTemplateView(TemplateView):

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['team'] = models.AboutModel.objects.all()

        return context
    
    template_name = 'pages/about.html'

class ContactTemplateView(CreateView):
    model = models.ContactModel
    fields = ['name', 'email', 'message','subject']
    template_name = 'pages/contact.html'
    success_url = reverse_lazy('pages:contact')

    def form_valid(self, form):
        messages.success(self.request,'Your message has been sent successfully.')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        for error in form.errors:
            messages.error(self.request,error)
        return super().form_invalid(form)
    
