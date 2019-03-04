from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Create your views here.

def news(request):
	posts = Post.objects.all()
	return render(request, "news/news.html", {'posts':posts})

def news_post(request, post_id):
	post = get_object_or_404(Post, id=post_id)
	return render(request, "news/news_post.html", {'post':post})

def category(request, category_id):
	category = get_object_or_404(Category, id=category_id)
	return render(request, "news/category.html", {'category': category})