from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from .models import *
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
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


class StudioUpdate(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
    template_name = 'studio_form.html'
    model = MusicalStudio

    def get_success_url(self):
        return reverse_lazy('studio_detail', kwargs={'pk': self.object.pk})


class MaterialUpdate(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
    template_name = 'material_form.html'
    model = MusicalMaterial

    def get_success_url(self):
        return reverse_lazy('material_detail', kwargs={'pk': self.object.pk})


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


class MaterialCreate(LoginRequiredMixin, CreateView):
    model = MusicalMaterial
    template_name = 'material_form.html'
    form_class = MaterialForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(MaterialCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('material_detail', kwargs={'pk': self.object.pk})


class MaterialDelete(DeleteView):
    model = MusicalMaterial
    success_url = reverse_lazy('material_list')

    def get_template_names(self):
        return ['musicalmaterial_confirm_delete.html']


class HoursListView(ListView):
    model = HoursRecord
    template_name = 'hours_list.html'
    context_object_name = 'hours'


class HourRecordCreate(LoginRequiredMixin, CreateView):
    model = HoursRecord
    template_name = 'hour_record_form.html'
    form_class = HourRecordForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(HourRecordCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('hours_list')


class HourUpdateView(UpdateView):
    model = HoursRecord
    template_name = 'hour_record_form.html'
    fields = ['date', 'hours', 'technician']

    def get_success_url(self):
        return reverse_lazy('hours_list')


class HourDeleteView(DeleteView):
    model = HoursRecord
    template_name = 'hour_record_delete.html'
    success_url = reverse_lazy('hours_list')


class ReceipListView(ListView):
    model = Receip
    template_name = 'finance/financial_data_list.html'
    context_object_name = 'factures'

class ReceipDetailView(DetailView): #pk auto
    model = Receip
    template_name = 'finance/financial_data_detail.html'
    context_object_name = 'Receip'

class ReceipCreateView(CreateView):
    model = Receip
    template_name = 'finance/financial_data_form.html'
    fields = ['name', 'data', 'subject', 'cost']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ReceipCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('financial_data_list')

class ReceipUpdateView(UpdateView):
    model = Receip
    template_name = 'finance/financial_data_form.html'
    fields = ['name', 'data', 'subject', 'cost']

    def get_success_url(self):
        return reverse_lazy('financial_data_list')

class ReceipDelateView(DeleteView):
    model = Receip
    template_name = 'finance/financial_data_remove.html'
    success_url = reverse_lazy('financial_data_list')


