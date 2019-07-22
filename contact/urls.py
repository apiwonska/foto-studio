from django.urls import path

from .views import contact

app_name = 'contact'
urlpatterns = [
    path('kontakt/', contact, name='contact'),
]
