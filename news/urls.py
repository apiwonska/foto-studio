from django.urls import path
from . import views

urlpatterns = [
    path('aktualnosci/', views.news, name='news'),
    path('aktualnosci/post/<int:post_id>/', views.news_post, name='news_post'),
    path('aktualnosci/kategoria/<int:category_id>/', views.category, name='category'),
]