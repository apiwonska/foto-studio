from django.db import models


class Link(models.Model):

    key = models.SlugField(max_length=100, unique=True,
                           verbose_name='nazwa klucza')
    name = models.CharField(
        max_length=200, verbose_name='sieć społecznościowa')
    url = models.URLField(max_length=200, null=True,
                          blank=True, verbose_name='link')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='data utworzenia')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='data aktualizacji')

    class Meta:
        verbose_name = 'link'
        verbose_name_plural = 'linki'
        ordering = ['name']

    def __str__(self):
        return self.name
