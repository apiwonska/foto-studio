from django.shortcuts import render
from .models import Price_list, Price

# Create your views here.

def prices(request):
	price_lists = Price_list.objects.all()
	prices = Price.objects.all()
	return render(request, "prices/prices.html", {'price_lists':price_lists, 'prices': prices})
