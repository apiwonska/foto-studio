from django.views.generic import ListView

from .models import Staff


class AboutListView(ListView):

    model = Staff
