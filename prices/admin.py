from django.contrib import admin

from .models import Price, PriceList


admin.site.register(PriceList)
admin.site.register(Price)
