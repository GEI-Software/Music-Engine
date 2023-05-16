from django import forms
from .models import *


class StudioForm(forms.ModelForm):
    class Meta:
        model = MusicalStudio
        fields = ['name', 'capacity', 'type', 'incorporated_material']


class MaterialForm(forms.ModelForm):
    class Meta:
        model = MusicalMaterial
        fields = ['name', 'type']


class HourRecordForm(forms.ModelForm):
    class Meta:
        model = HoursRecord
        fields = ['date', 'hours', 'technician']


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['sala', 'material', 'tecnic', 'data', 'hora_inici', 'hora_fi', 'reservat']
