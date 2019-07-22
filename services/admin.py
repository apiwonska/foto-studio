from django.contrib import admin

from .models import FotoPortrait, FotoStudio, FotoWedding


class FotoPortraitAdmin(admin.ModelAdmin):

    list_display = ['__str__', 'title', 'author']


class FotoWeddingAdmin(admin.ModelAdmin):

    list_display = ['__str__', 'title', 'author']


class FotoStudioAdmin(admin.ModelAdmin):

    list_display = ['__str__', 'title', 'author']


admin.site.register(FotoPortrait, FotoPortraitAdmin)
admin.site.register(FotoWedding, FotoWeddingAdmin)
admin.site.register(FotoStudio, FotoStudioAdmin)
