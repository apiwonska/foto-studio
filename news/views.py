from django.views.generic import ListView, DetailView

from .models import Post, Category


class NewsListView(ListView):

    model = Post
    paginate_by = 4
    paginate_orphans = 1
    ordering = ['-published']


class PostDetailView(DetailView):

    model = Post


class CategoryDetailView(DetailView):

    model = Category
