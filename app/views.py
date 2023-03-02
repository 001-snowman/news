from django.shortcuts import render
from app.models import category, news

# Create your views here.

def index(request):
    data={
        'categoryData':category.objects.all(),
        'worldNews':news.objects.filter(news_category=1)
    }
    return render(request, "index.html", data)