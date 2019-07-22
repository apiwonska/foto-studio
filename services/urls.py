from django.urls import path

from .views import FotoPortraitListView, FotoStudioListView, FotoWeddingListView

app_name = 'services'
urlpatterns = [
    path('oferta/sesje-fotograficzne/',
         FotoPortraitListView.as_view(), name='foto_portrait'),
    path('oferta/fotografia-slubna/',
         FotoWeddingListView.as_view(), name='foto_weddings'),
    path('oferta/studio-wynajem/', FotoStudioListView.as_view(), name='lease'),
]
