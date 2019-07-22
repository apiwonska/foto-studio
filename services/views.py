from django.views.generic import ListView

from .models import FotoPortrait, FotoStudio, FotoWedding


class FotoPortraitListView(ListView):

    model = FotoPortrait


class FotoWeddingListView(ListView):

    model = FotoWedding


class FotoStudioListView(ListView):

    model = FotoStudio
