from django.urls import path
from . import views

urlpatterns = [
    path('cennik/', views.prices, name='prices'),
]
