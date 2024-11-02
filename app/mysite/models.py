from django.db import models

from users.models import User


class Game(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название")
    slug = models.SlugField(unique=True, blank=True, null=True, verbose_name="URL")
    description = models.TextField(blank=True, default='Нет описания', verbose_name="Описание")
    iamge = models.ImageField(upload_to='foto', blank=True, max_length=1000, verbose_name="Изображение")
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="Время публикации")
    category = models.ForeignKey(to="CategoryGame", on_delete=models.CASCADE, verbose_name="Категория")
    avtor = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='Автор', blank=True, null=True)
    
    class Meta:
        db_table = 'Game'
        
    def __str__(self):
        return self.name
    
    
class CategoryGame(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название")
    slug = models.SlugField(unique=True, blank=True, null=True, verbose_name="URL")
    
    class Meta:
        db_table = "CategoryGame"
        
    def __str__(self):
        return self.name
    