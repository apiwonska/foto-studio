from django.urls import path
from .views import PricesPageView

urlpatterns = [
    path('cennik/', PricesPageView.as_view(), name='prices'),
]
