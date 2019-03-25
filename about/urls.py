from django.urls import path
from .views import AboutListView

urlpatterns = [
    path('o-nas/', AboutListView.as_view(), name='about'),
]
