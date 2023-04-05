from django.contrib import admin
from .models import *


class StudioAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'type', 'incorporated_material')


class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')


admin.site.register(MusicalStudio, StudioAdmin)
admin.site.register(MusicalMaterial, MaterialAdmin)
admin.site.register(ResourceManager)
admin.site.register(Technician)
