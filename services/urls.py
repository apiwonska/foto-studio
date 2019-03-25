from django.urls import path
from .views import GalleryPortraitListView, GalleryWeddingsListView, GalleryStudioListView

app_name = 'services'
urlpatterns = [
    path('oferta/sesje-fotograficzne/', GalleryPortraitListView.as_view(), name='foto_studio'),
    path('oferta/fotografia-slubna/', GalleryWeddingsListView.as_view(), name='foto_weddings'),
    path('oferta/studio-wynajem/', GalleryStudioListView.as_view(), name='lease'),
]