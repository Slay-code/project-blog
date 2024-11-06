from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from unidecode import unidecode

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
        ordering = ['-time_created']
        db_table = 'Game'
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("mysite:game_details", args=[self.pk, self.slug])
    
    # полезная хуйня
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.name))
        super().save(*args, **kwargs)
    
    
    
class CategoryGame(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название")
    slug = models.SlugField(unique=True, blank=True, null=True, verbose_name="URL")
    
    class Meta:
        db_table = "CategoryGame"
        
    def __str__(self):
        return self.name
    
    
    