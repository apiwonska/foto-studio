from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFit


class FotoDescription(models.Model):
    title = models.CharField(max_length=200, null=True,
                             blank=True, verbose_name='tytuł')
    author = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='autor')
    order = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name='kolejność na stronie')

    class Meta:
        abstract = True


class FotoPortrait(FotoDescription):

    image = ProcessedImageField(
        upload_to='img/services/portrait/',
        processors=[ResizeToFit(height=800, upscale=False)],
        format='JPEG',
        options={'quality': 60},
        verbose_name='zdjęcie')
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFit(width=355)],
        format='JPEG',
        options={'quality': 60})

    class Meta:
        verbose_name = "galeria - Fotografia Portretowa"
        verbose_name_plural = "galeria - Fotografia Portretowa"
        ordering = ['order']

    def __str__(self):
        return str(self.order) + ". Fotografia Portretowa"


class FotoWedding(FotoDescription):

    image = ProcessedImageField(
        upload_to='img/services/wedding/',
        processors=[ResizeToFit(height=800, upscale=False)],
        format='JPEG',
        options={'quality': 60},
        verbose_name='zdjęcie')
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFit(width=355)],
        format='JPEG',
        options={'quality': 60})

    class Meta:
        verbose_name = "galeria - Fotografia Weselna"
        verbose_name_plural = "galeria - Fotografia Weselna"
        ordering = ['order']

    def __str__(self):
        return str(self.order) + ". Fotografia Weselna"


class FotoStudio(FotoDescription):

    image = ProcessedImageField(
        upload_to='img/services/studio/',
        processors=[ResizeToFit(height=800, upscale=False)],
        format='JPEG',
        options={'quality': 60},
        verbose_name='zdjęcie')
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFit(width=355)],
        format='JPEG',
        options={'quality': 60})

    class Meta:
        verbose_name = "galeria - Studio"
        verbose_name_plural = "galeria - Studio"
        ordering = ['order']

    def __str__(self):
        return str(self.order) + ". Studio"
