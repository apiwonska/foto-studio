from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill


class Staff(models.Model):
    name = models.CharField(max_length=200, verbose_name='imię')
    job_title = models.CharField(max_length=200, verbose_name='stanowisko')
    description = models.TextField(verbose_name='opis')
    image = ProcessedImageField(
        upload_to='img/about/',
        processors=[ResizeToFill(width=350, height=466)],
        format='JPEG',
        options={'quality': 60},   
        verbose_name='plik')
    order = models.PositiveSmallIntegerField(
        verbose_name='kolejność na stronie')

    class Meta:
        verbose_name = 'pracownik'
        verbose_name_plural = 'pracownicy'
        ordering = ['order']

    def __str__(self):
        return str(self.order) + '. Pracownicy: ' + self.name
