from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone

from .models import *
from django.views.generic import ListView, UpdateView


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


class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
        return obj


class LoginRequiredCheckIsOwnerUpdateView(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
    template_name = 'studio_form.html'
    model = MusicalStudio
    def get_success_url(self):
        return reverse_lazy('studio_detail', kwargs={'pk': self.object.pk})


class ReservaListView(ListView):
    model = Reserva
    template_name = 'reserva_list.html'
    context_object_name = 'reserves'
