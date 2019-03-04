from django.db import models
from django.core.validators import FileExtensionValidator


class GalleryPortrait(models.Model):
	title = models.CharField(max_length=200, null=True, blank=True, verbose_name='Tytuł')
	author = models.CharField(max_length=100, null=True, blank=True, verbose_name='Autor')
	order = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='Kolejność na stronie')
	image = models.ImageField(
		upload_to='img/portraits/', 
		validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png','gif'])], 
		verbose_name='Plik')
	class Meta:
		verbose_name = "Galeria - Fotografia Portretowa"
		verbose_name_plural = "Galeria - Fotografia Portretowa"
		ordering = ['order']

	def __str__(self):
		return str(self.order) + ". Fotografia Portretowa"
		

class GalleryWeddings(models.Model):
	title = models.CharField(max_length=200, null=True, blank=True, verbose_name='Tytuł')
	author = models.CharField(max_length=100, null=True, blank=True, verbose_name='Autor')
	order = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='Kolejność na stronie')
	image = models.ImageField(
		upload_to='img/weddings/', 
		validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png','gif'])], 
		verbose_name='Plik')
	class Meta:
		verbose_name = "Galeria - Fotografia Weselna"
		verbose_name_plural = "Galeria - Fotografia Weselna"
		ordering = ['order']

	def __str__(self):
		return str(self.order) + ". Fotografia Weselna"

class GalleryStudio(models.Model):
	title = models.CharField(max_length=200, null=True, blank=True, verbose_name='Tytuł')
	author = models.CharField(max_length=100, null=True, blank=True, verbose_name='Autor')
	order = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='Kolejność na stronie')
	image = models.ImageField(
		upload_to='img/studio/', 
		validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png','gif'])], 
		verbose_name='Plik')
	class Meta:
		verbose_name = "Galeria - Studio"
		verbose_name_plural = "Galeria - Studio"
		ordering = ['order']

	def __str__(self):
		return str(self.order) + ". Studio"