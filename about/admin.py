from django.contrib import admin

from .models import Staff


class StaffAdmin(admin.ModelAdmin):

    list_display = ('__str__', 'job_title')


admin.site.register(Staff, StaffAdmin)
