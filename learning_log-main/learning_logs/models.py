from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):
    """Модель для топика."""
    text = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add = True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Entry(models.Model):
    """Информация, изученная пользователем по теме"""
    topics = models.ForeignKey(Topic, on_delete = models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """Возвращает строковое представление модели."""
        return f"{self.text[:50]}..."