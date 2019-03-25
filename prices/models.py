from django.db import models


# Create your models here.
class Price_list(models.Model):
	title_price_list = models.CharField(max_length=100, verbose_name='nazwa Cennika')
	order = models.PositiveSmallIntegerField(verbose_name = 'kolejność tabel')

	class Meta:
		verbose_name = "cennik - kategoria"
		verbose_name_plural = "cenniki - kategorie"
		ordering = ['order']

	def __str__(self):
		return str(self.order)+ '. ' + self.title_price_list
    
    

class Price(models.Model):
	price_list = models.ForeignKey(Price_list, on_delete=models.CASCADE, verbose_name='cennik')
	service = models.CharField(max_length=200, verbose_name='usługa')
	service_details = models.CharField(null=True, blank=True, max_length=200, verbose_name='szczegóły') 
	price = models.CharField(max_length=20,verbose_name='cena')
	order = models.PositiveSmallIntegerField(verbose_name = 'kolejność ceny w tabeli')

	class Meta:
		verbose_name = "cena"
		verbose_name_plural = "ceny"
		ordering = ['price_list','order']

	def __str__(self):
		return  f'{self.price_list} - {self.order}.Cena: ' + self.service


    