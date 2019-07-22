from django.urls import path

from .views import PricesPageView

app_name = 'prices'
urlpatterns = [
    path('cennik/', PricesPageView.as_view(), name='prices'),
]
