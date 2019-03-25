from django.views.generic import ListView, DetailView
from .models import Post, Category

class NewsListView(ListView):

    model = Post

class PostDetailView(DetailView):

	model = Post

class CategoryDetailView(DetailView):

    model = Category

