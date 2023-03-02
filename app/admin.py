from django.contrib import admin
from app.models import category, news

# Register your models here.

@admin.register(category)
class adminCategory(admin.ModelAdmin):
    list_display=['title', 'image']

@admin.register(news)
class adminNews(admin.ModelAdmin):
    list_display=['news_category', 'news_title', 'intro_text', 'detailed_news', 'image']