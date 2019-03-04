from django.contrib import admin
from .models import GalleryPortrait, GalleryWeddings, GalleryStudio

# Register your models here.
admin.site.register(GalleryPortrait)
admin.site.register(GalleryWeddings)
admin.site.register(GalleryStudio)