from django.contrib import admin

from .models import Project

admin.site.site_header = 'Defi_Tracker Admin'
admin.site.site_title = 'Defi_Tracker Admin Area'
admin.site.index_title = 'Welcome to the Defi_Tracker Admin area'

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [('Name', {'fields': ['name']}), ('tvl', {'fields': ['tvl']}),]

admin.site.register(Project, ProjectAdmin)