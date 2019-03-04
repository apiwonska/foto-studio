from django.shortcuts import render

# Create your views here.

# home
# about
# offer-sessions
# offer-weddings
# offer-lease
# pricing
# news
# news_post
# contact

def home(request):
	return render(request, "core/home.html")





