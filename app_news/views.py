from typing import Any
from django.db.models.query import Q
from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView


from app_news import models
from app_news.forms import NewsCommentForm

class NewsListView(ListView):
    template_name = 'news/new.html'
    model = models.NewsModel
    context_object_name = 'news'
    paginate_by = 5

    def get_queryset(self):
        news = models.NewsModel.objects.all()

        cat = self.request.GET.get('cat')
        tag = self.request.GET.get('tag')
        q = self.request.GET.get('q')

        if cat:
            news = models.NewsModel.objects.filter(categories=cat)

        if tag:
            news = models.NewsModel.objects.filter(tags=tag)

        if q:
            news = models.NewsModel.published.filter(
                Q(title__icontains=q) | Q(body__icontains=q)
            )
        
        return news
            
        
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['categories'] = models.NewsCategoryModel.objects.all()
        context['tags'] = models.NewsTagModel.objects.all()
        context['recent_posts'] = models.NewsModel.objects.order_by('-created_at')[:4]

        return context
    

class NewsDetailView(DetailView):
    template_name = 'news/new_detail.html'
    model = models.NewsModel
    context_object_name = 'new'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['categories'] = models.NewsCategoryModel.objects.all()
        context['tags'] = models.NewsTagModel.objects.all()
        context['recent_posts'] = models.NewsModel.objects.order_by('-created_at')[:4]
        
       
        return context
    
    def get_queryset(self):
        news = models.NewsModel.published.all()
        cat = self.request.GET.get('cat')
        tag = self.request.GET.get('tag')
        q = self.request.GET.get('q')

        if cat:
            news = models.NewsModel.published.filter(categories=cat)
        if tag:
            news = models.NewsModel.published.filter(tags=tag)

        if q:
            news = models.NewsModel.published.filter(
                Q(title__icontains=q) | Q(body__icontains=q)
            )
    
        return news
    
    def post(self, *args, **kwargs):
        if not self.request.user.is_authenticated:  
            return redirect("users:login")

        form = NewsCommentForm(self.request.POST)
        news_id = self.request.POST.get("news_id") 
    

        if not news_id:  
            return self.get(self.request,*args, **kwargs)

        try:
            news = models.NewsModel.objects.get(id=news_id) 
        except models.NewsModel.DoesNotExist:
            return self.get(self.request, *args, **kwargs)  

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = self.request.user
            comment.news = news 
            comment.save()
            return redirect("news:detail", pk=news_id)
            

        return self.get(self.request, *args, **kwargs)
