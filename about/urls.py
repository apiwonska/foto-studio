from django.urls import path
from . import views

urlpatterns = [
    path('o-nas/', views.about, name='about'),
]
