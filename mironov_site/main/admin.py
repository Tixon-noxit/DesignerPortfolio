from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import *
from django.utils.safestring import mark_safe


# Register your models here.


class SiteSettingsAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class EducationAdmin(admin.ModelAdmin):
    list_display = ('theNameOfTheInstitution', 'periodOfStudy', 'receivedSkills', 'is_published')
    list_display_links = ('theNameOfTheInstitution',)
    search_fields = ('theNameOfTheInstitution',)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_html_photo', 'is_published','time_create')
    list_display_links = ('title', 'get_html_photo')
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}
    fields = ('title', 'slug', 'Preview', 'get_html_photo', 'Photos1', 'Photos2', 'Photos3', 'Photos4', 'Photos5', 'Photos6', 'Photos7', 'Photos8', 'Photos9', 'Photos10', 'is_published')  #
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')  #
    
    def get_html_photo(self, object):
        if object.Preview:
            return mark_safe(f'<img src="{object.Preview.url}" style="max-height: 100px;">')

    get_html_photo.short_description = "Актуальное превью"
    

class CreationAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_html_photo', 'is_published','time_create')
    list_display_links = ('title', 'get_html_photo')
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}
    fields = ('title', 'slug', 'Preview', 'get_html_photo', 'Photos1', 'Photos2', 'Photos3', 'Photos4', 'Photos5', 'Photos6', 'Photos7', 'Photos8', 'Photos9', 'Photos10', 'is_published')  #
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')  #
    
    def get_html_photo(self, object):
        if object.Preview:
            return mark_safe(f'<img src="{object.Preview.url}" style="max-height: 100px;">')

    get_html_photo.short_description = "Актуальное превью"
    


class PartnersAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published')
    list_display_links = ('name',)
    search_fields = ('name',)



admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(SiteSettings, SiteSettingsAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Partners, PartnersAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Creation, CreationAdmin)
