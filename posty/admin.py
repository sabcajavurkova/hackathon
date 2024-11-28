from django.contrib import admin

from .models import Report

class ReportAdmin(admin.ModelAdmin):
    list_display = ('address', 'text', 'username')


admin.site.register(Report, ReportAdmin)
