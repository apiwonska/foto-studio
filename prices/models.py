from django.db import models


# Create your models here.
class Price_list(models.Model):
	title_price_list = models.CharField(max_length=100, verbose_name='Nazwa Cennika')
	order = models.PositiveSmallIntegerField(verbose_name = 'Kolejność tabel')

	class Meta:
		verbose_name = "Cennik - kategoria"
		verbose_name_plural = "Cenniki - kategorie"
		ordering = ['order']

	def __str__(self):
		return str(self.order)+ '. ' + self.title_price_list
    
    

class Price(models.Model):
	price_list = models.ForeignKey(Price_list, on_delete=models.CASCADE, verbose_name='Cennik')
	service = models.CharField(max_length=200, verbose_name='Usługa')
	service_details = models.CharField(null=True, blank=True, max_length=200, verbose_name='Szczegóły') 
	price = models.CharField(max_length=20,verbose_name='Cena')
	order = models.PositiveSmallIntegerField(verbose_name = 'Kolejność ceny w tabeli')

	class Meta:
		verbose_name = "Cena"
		verbose_name_plural = "Ceny"
		ordering = ['price_list','order']

	def __str__(self):
		return  f'{self.price_list} - {self.order}.Cena: ' + self.service


    