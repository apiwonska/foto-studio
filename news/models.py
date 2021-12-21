from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill


class Category(models.Model):

    name = models.CharField(max_length=50, verbose_name='kategoria')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='data utworzenia')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='data utworzenia')

    class Meta:
        verbose_name = "post: Kategoria"
        verbose_name_plural = "posty: Kategorie"
        ordering = ['-created']

    def __str__(self):
        return self.name


class Post(models.Model):

    title = models.CharField(max_length=200, verbose_name='tytuł')
    content = RichTextField(verbose_name='treść')
    categories = models.ManyToManyField(
        Category,
        verbose_name='kategoria',
        related_name='get_posts')
    author = models.ForeignKey(
        User,
        verbose_name='autor',
        on_delete=models.CASCADE)
    image = ProcessedImageField(
        upload_to='img/news',
        processors=[ResizeToFill(920, 460)],
        format='JPEG',
        options={'quality': 60},
        null=True,
        blank=True,
        verbose_name='zdjęcie')
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(350, 263)],
        format='JPEG',
        options={'quality': 60})
    published = models.DateTimeField(
        verbose_name='data publikacji', default=timezone.now)
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='data utworzenia')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='data utworzenia')

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posty"
        ordering = ['-published']

    def __str__(self):
        return self.title
