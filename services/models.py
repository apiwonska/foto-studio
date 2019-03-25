from django.db import models
from django.core.validators import FileExtensionValidator


class GalleryPortrait(models.Model):
	title = models.CharField(max_length=200, null=True, blank=True, verbose_name='tytuł')
	author = models.CharField(max_length=100, null=True, blank=True, verbose_name='autor')
	order = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='kolejność na stronie')
	image = models.ImageField(
		upload_to='img/portraits/', 
		validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png','gif'])], 
		verbose_name='plik')
	class Meta:
		verbose_name = "galeria - Fotografia Portretowa"
		verbose_name_plural = "galeria - Fotografia Portretowa"
		ordering = ['order']

	def __str__(self):
		return str(self.order) + ". Fotografia Portretowa"
		

class GalleryWeddings(models.Model):
	title = models.CharField(max_length=200, null=True, blank=True, verbose_name='tytuł')
	author = models.CharField(max_length=100, null=True, blank=True, verbose_name='autor')
	order = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='kolejność na stronie')
	image = models.ImageField(
		upload_to='img/weddings/', 
		validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png','gif'])], 
		verbose_name='plik')
	class Meta:
		verbose_name = "galeria - Fotografia Weselna"
		verbose_name_plural = "galeria - Fotografia Weselna"
		ordering = ['order']

	def __str__(self):
		return str(self.order) + ". Fotografia Weselna"

class GalleryStudio(models.Model):
	title = models.CharField(max_length=200, null=True, blank=True, verbose_name='tytuł')
	author = models.CharField(max_length=100, null=True, blank=True, verbose_name='autor')
	order = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='kolejność na stronie')
	image = models.ImageField(
		upload_to='img/studio/', 
		validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png','gif'])], 
		verbose_name='plik')
	class Meta:
		verbose_name = "galeria - Studio"
		verbose_name_plural = "galeria - Studio"
		ordering = ['order']

	def __str__(self):
		return str(self.order) + ". Studio"