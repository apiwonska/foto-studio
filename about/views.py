from django.views.generic import ListView, TemplateView
from .models import Staff

class AboutListView(ListView):

    model = Staff

