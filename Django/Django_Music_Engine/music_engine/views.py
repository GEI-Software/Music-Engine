from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from .models import *
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from .forms import *


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


class LlistaTecnics(ListView):
    model = technical_personnel
    template_name = 'detall_tecnic.html'
    context_object_name = 'tecnic'


class AssignmentListView(ListView):
    model = Assignment
    template_name = 'assignment_list.html'
    context_object_name = 'assignments'
    ordering = ['date']


class StudioCreate(LoginRequiredMixin, CreateView):
    model = MusicalStudio
    template_name = 'studio_form.html'
    form_class = StudioForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(StudioCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('studio_detail', kwargs={'pk': self.object.pk})


class StudioDelete(DeleteView):
    model = MusicalStudio
    success_url = reverse_lazy('studio_list')

    def get_template_names(self):
        return ['musicalstudio_confirm_delete.html']
