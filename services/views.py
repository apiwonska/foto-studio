from django.shortcuts import render
from .models import GalleryPortrait, GalleryWeddings, GalleryStudio

# Create your views here.

def services_foto_studio(request):
	gallery_portrait = GalleryPortrait.objects.all()
	return render(request, "services/services_foto_studio.html", {'gallery_portrait': gallery_portrait})

def services_foto_weddings(request):
	gallery_weddings = GalleryWeddings.objects.all()
	return render(request, "services/services_foto_weddings.html", {'gallery_weddings': gallery_weddings})

def services_lease(request):
	gallery_studio = GalleryStudio.objects.all()
	return render(request, "services/services_lease.html", {'gallery_studio': gallery_studio})