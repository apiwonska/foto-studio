from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='kategoria')
    created = models.DateTimeField(auto_now_add=True, verbose_name='data utworzenia')
    updated = models.DateTimeField(auto_now=True, verbose_name='data utworzenia')

    class Meta:
        verbose_name = "post: Kategoria"
        verbose_name_plural = "posty: Kategorie"
        ordering = ['-created']

    def __str__(self):
        return self.name


class Post(models.Model):    
    title = models.CharField(max_length=200, verbose_name='tytuł') 
    content = models.TextField(verbose_name='tekst')
    categories = models.ManyToManyField(
        Category, 
        verbose_name='kategoria',
        related_name='get_posts')       
    author = models.ForeignKey(
        User, 
        verbose_name='autor', 
        on_delete=models.CASCADE)

    image = models.ImageField(
        upload_to='img/news/', 
        verbose_name='zdjęcie')
    image_small = models.ImageField(
        upload_to='img/news/', 
        verbose_name='zdjęcie małe')

    published = models.DateTimeField(verbose_name='data publikacji', default=timezone.now)
    created = models.DateTimeField(auto_now_add=True, verbose_name='data utworzenia')
    updated = models.DateTimeField(auto_now=True, verbose_name='data utworzenia')

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posty"

    def __str__(self):
        return self.title

    def content_short(self):
        content_short_words = self.content.split(' ')[:70]
        return ' '.join(content_short_words)
    
    