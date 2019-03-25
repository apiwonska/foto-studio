from django.views.generic import ListView, DetailView
from .models import Post, Category

class NewsListView(ListView):

    model = Post
    paginate_by = 2

class PostDetailView(DetailView):

	model = Post

class CategoryDetailView(DetailView):

    model = Category



