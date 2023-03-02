from django.db import models

# Create your models here.

class category(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.title

class news(models.Model):
    news_category=models.ForeignKey(category, on_delete=models.CASCADE)
    news_title=models.CharField(max_length=100)
    intro_text=models.CharField(max_length=500)
    detailed_news=models.CharField(max_length=10000)
    image=models.ImageField(blank=True, null=True, upload_to='images/')