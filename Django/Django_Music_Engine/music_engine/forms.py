from django import forms
from django.contrib.auth.forms import UserCreationForm

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

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=40, widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

