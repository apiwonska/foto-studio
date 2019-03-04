from django.urls import path
from . import views

urlpatterns = [
    path('oferta/sesje-fotograficzne/', views.services_foto_studio, name='services_foto_studio'),
    path('oferta/fotografia-slubna/', views.services_foto_weddings, name='services_foto_weddings'),
    path('oferta/studio-wynajem/', views.services_lease, name='services_lease'),
]