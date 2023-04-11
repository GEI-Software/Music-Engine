from django.contrib import admin
from .models import *


class StudioAdmin(admin.ModelAdmin):
    def inc_display(self, obj):
        return ', '.join([inc_mat.name for inc_mat in obj.incorporated_material.all()])

    inc_display.short_description = 'Incorporated Material'
    list_display = ('name', 'capacity', 'type', 'inc_display')


class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')


class ReservaAdmin(admin.ModelAdmin):
    list_display = ('usuari', 'sala', 'data', 'hora_inici', 'hora_fi', 'reservat')


class LlistatTecnics(admin.ModelAdmin):
    list_display = ('dni', 'name', 'last_name')


admin.site.register(MusicalStudio, StudioAdmin)
admin.site.register(MusicalMaterial, MaterialAdmin)
admin.site.register(Reserva, ReservaAdmin)
admin.site.register(technical_personnel, LlistatTecnics)
