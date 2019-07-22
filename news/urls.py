from django.urls import path

from .views import CategoryDetailView, NewsListView, PostDetailView

app_name = 'news'
urlpatterns = [
    path('aktualnosci/', NewsListView.as_view(), name='posts'),
    path('aktualnosci/post/<int:pk>/', PostDetailView.as_view(), name='post'),
    path('aktualnosci/kategoria/<int:pk>/',
         CategoryDetailView.as_view(), name='category'),
]
