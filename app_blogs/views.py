from typing import Any
from django.shortcuts import redirect
from django.views.generic import ListView,DetailView
from django.db.models.query import Q


from app_blogs import models
from app_blogs import forms

class BlogListView(ListView):
    template_name = 'blogs/blog.html'
    model = models.BlogModel
    context_object_name = 'blogs'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = models.BlogCategoryModel.objects.all()
        context['tags'] = models.BlogTagModel.objects.all()
        context['recent_posts'] = models.BlogModel.objects.order_by('-created_at')[:4]
  
        return context
    
    def get_queryset(self):
        blogs = models.BlogModel.objects.all()
        cat = self.request.GET.get('cat')
        tag = self.request.GET.get('tag')
        q = self.request.GET.get('q')

        if cat:
            blogs = models.BlogModel.objects.filter(categories=cat)
        if tag:
            blogs = models.BlogModel.objects.filter(tags=tag)

        if q:
            blogs = models.BlogModel.objects.filter(
                Q(title__icontains=q) | Q(description__icontains=q)
            )
    
        return blogs

    
class BlogDetailView(DetailView):
    model = models.BlogModel
    template_name = 'blogs/blog_detail.html'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = models.BlogCategoryModel.objects.all()
        context['tags'] = models.BlogTagModel.objects.all()
        context['recent_posts'] = models.BlogModel.objects.order_by('-created_at')[:4]
        
        return context
    
    def post(self, *args, **kwargs):
        if not self.request.user.is_authenticated:  
            return redirect("users:login")

        form = forms.BlogsCommentForm(self.request.POST)
        blog_id = self.request.POST.get("blog_id") 

        if not blog_id:  
            return self.get(self.request,*args, **kwargs)

        try:
            blog = models.BlogModel.objects.get(id=blog_id)

        except models.BlogModel.DoesNotExist:
            return self.get(self.request, *args, **kwargs)  

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = self.request.user
            comment.blog = blog
            comment.save()
            return redirect("blogs:detail", pk=blog.id)
            

        return self.get(self.request, *args, **kwargs)

   


    