from django.urls import path
from . import views

app_name = 'contact'
urlpatterns = [
    path('kontakt/', views.contact, name='contact'),
]
