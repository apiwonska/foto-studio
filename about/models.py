from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class Staff(models.Model):
	name = models.CharField(max_length=200, verbose_name='imię')
	job_title = models.CharField(max_length=200, verbose_name='stanowisko')
	description = models.TextField(verbose_name='opis')
	image = models.ImageField(
		upload_to='img/about/', 
		validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png','gif'])], 
		verbose_name='plik')
	order = models.PositiveSmallIntegerField(verbose_name = 'kolejność na stronie')

	class Meta:
		verbose_name='pracownik'
		verbose_name_plural='pracownicy'
		ordering = ['order']

	def __str__(self):
		return str(self.order) + '. Pracownicy: ' + self.name

		
