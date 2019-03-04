from django.shortcuts import render
from .models import Staff

# Create your views here.

def about(request):
	staff = Staff.objects.all()
	return render(request, "about/about.html", {'staff':staff})
