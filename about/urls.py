from django.urls import path

from .views import AboutListView

app_name = 'about'
urlpatterns = [
    path('o-nas/', AboutListView.as_view(), name='about'),
]
