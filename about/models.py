from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class Staff(models.Model):
	name = models.CharField(max_length=200, verbose_name='Imię')
	job_title = models.CharField(max_length=200, verbose_name='Stanowisko')
	description = models.TextField(verbose_name='Opis')
	image = models.ImageField(
		upload_to='img/about/', 
		validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png','gif'])], 
		verbose_name='Plik')
	order = models.PositiveSmallIntegerField(verbose_name = 'Kolejność na stronie')

	class Meta:
		verbose_name='pracownik'
		verbose_name_plural='pracownicy'
		ordering = ['order']

	def __str__(self):
		return str(self.order) + '. Pracownicy: ' + self.name

		
