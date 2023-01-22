from django.contrib import admin
from .models import *
# Register your models here.


class SiteSettingsAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class EducationAdmin(admin.ModelAdmin):
    list_display = ('theNameOfTheInstitution', 'periodOfStudy', 'receivedSkills', 'is_published')
    list_display_links = ('theNameOfTheInstitution',)
    search_fields = ('theNameOfTheInstitution',)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_create', 'is_published')
    list_display_links = ('title',)
    search_fields = ('title',)


class PartnersAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published')
    list_display_links = ('name',)
    search_fields = ('name',)


admin.site.register(SiteSettings, SiteSettingsAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Partners, PartnersAdmin)
admin.site.register(Project, ProjectAdmin)

