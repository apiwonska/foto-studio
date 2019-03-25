from django.views.generic import ListView
from .models import GalleryPortrait, GalleryWeddings, GalleryStudio

class GalleryPortraitListView(ListView):

    model = GalleryPortrait

class GalleryWeddingsListView(ListView):

    model = GalleryWeddings

class GalleryStudioListView(ListView):

    model = GalleryStudio

