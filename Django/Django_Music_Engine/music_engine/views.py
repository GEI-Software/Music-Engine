from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.generic import ListView


def studio_detail(request, pk):
    studio = get_object_or_404(MusicalStudio, pk=pk)
    return render(request, 'studio_detail.html', {'studio': studio})


class StudioListView(ListView):
    model = MusicalStudio
    template_name = 'studio_list.html'
    context_object_name = 'studios'


def material_detail(request, pk):
    material = get_object_or_404(MusicalMaterial, pk=pk)
    return render(request, 'material_detail.html', {'material': material})


class MaterialListView(ListView):
    model = MusicalMaterial
    template_name = 'material_list.html'
    context_object_name = 'materials'


def home(request):
    return render(request, 'base.html')


class HomeView:
    template_name = 'base.html'
