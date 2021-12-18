from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

class Articles(models.Model):
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=100, blank=True)
    text = models.TextField()
    photo = models.ImageField(upload_to='images/', blank=True)
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", args=[str(self.pk)])
    
# Create your models here.