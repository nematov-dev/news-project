from app_news import models

def most_recents(request):
    
    news = models.NewsModel.published.all().order_by('-publish_time')[:3]
    context = {
        "news":news,
    }
    return context
