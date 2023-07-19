from django.contrib import admin
from .models import *


class EducationAdmin(admin.ModelAdmin):
    list_display = ('id', 'theNameOfTheInstitution')
    list_display_links = ('id', 'theNameOfTheInstitution')
    search_fields = ('id', 'theNameOfTheInstitution')

class PartnersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')


# admin.site.register(Education, EducationAdmin)
# admin.site.register(Partners, PartnersAdmin)
