from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from .models import *
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from .forms import *
from datetime import datetime, timedelta
from datetime import date, timedelta
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Assesorament
from .forms import AssesoramentForm

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


def reserva_detail(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    return render(request, 'reserva_detail.html', {'reserva': reserva})


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


class CharacteristicTechinicalPersonview(ListView):
    model = technical_personnel
    template_name = 'characteristic_technical.html'
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


class ReceipDetailView(DetailView):  # pk auto
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


def calendario_tecnico(request):
    today = date.today()
    year = request.GET.get('year', today.year)
    month = request.GET.get('month', today.month)
    day = request.GET.get('day', today.day)
    date_obj = date(year=int(year), month=int(month), day=int(day))

    month_weeks = []
    # Calculate the first day of the current month
    first_day = date_obj.replace(day=1)
    # Calculate the weekday of the first day of the current month
    first_weekday = first_day.weekday()
    # Calculate the number of days in the current month
    days_in_month = (date_obj.replace(day=28) + timedelta(days=4)).replace(day=1) - timedelta(days=1)
    # Calculate the number of weeks in the current month
    num_weeks = (first_weekday + days_in_month.day + 6) // 7
    # Create a list of weeks, where each week is a list of days
    for week in range(num_weeks):
        week_days = []
        for weekday in range(7):
            day_number = week * 7 + weekday - first_weekday + 1
            if day_number < 1 or day_number > days_in_month.day:
                week_days.append((None, None))
            else:
                day = date_obj.replace(day=day_number)
                url = url = reverse('disponibilidad', args=[day.year, day.month, day.day])

                week_days.append((day_number, url))
        month_weeks.append(week_days)

    return render(request, 'calendario_tecnico.html', {
        'date_obj': date_obj,
        'month_weeks': month_weeks,
    })


def disponibilidad_tecnico(request, year, month, day):
    date_obj = date(year=int(year), month=int(month), day=int(day))
    horas = []
    for i in range(0, 24, 2):
        try:
            disponibility = Disponibility.objects.get(date=date_obj, technician=request.user)
            horas.append({'hour': i, 'available': disponibility.available, 'record_id': disponibility.id})
        except HoursRecord.DoesNotExist:
            horas.append({'hour': i, 'available': True, 'record_id': None})
    if request.method == 'POST':
        for hora in horas:
            record_id = hora['record_id']
            available = request.POST.get(str(record_id))
            if available is not None:
                disponibility = Disponibility.objects.get(id=record_id)
                disponibility.available = available == 'on'
                disponibility.save()
    return render(request, 'disponibilidad_tecnico.html', {'date_obj': date_obj, 'horas': horas})


class ReservaCreate(LoginRequiredMixin, CreateView):
    model = Reserva
    template_name = 'reserva_form.html'
    form_class = ReservaForm

    def form_valid(self, form):
        form.instance.usuari = self.request.user
        return super(ReservaCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('reserva_list')


def serveis(request):
    return render(request, 'serveis.html')
def assesorament_list(request):
    # Obtener todos los asesoramientos del cliente actual (usuario)
    assesoraments = Assesorament.objects.filter(client_name=request.user)

    context = {
        'assesoraments': assesoraments
    }
    return render(request, 'assesorament_list.html', context)

def create_assesorament(request):
    if request.method == 'POST':
        form = AssesoramentForm(request.POST)
        if form.is_valid():
            assesorament = form.save(commit=False)
            assesorament.client_name = request.user
            assesorament.save()
            return redirect('assesorament_list')
    else:
        form = AssesoramentForm()
    
    context = {
        'form': form
    }
    return render(request, 'create_assesorament.html', context)

def edit_assesorament(request, assesorament_id):
    assesorament = Assesorament.objects.get(pk=assesorament_id)
    
    if request.method == 'POST':
        form = AssesoramentForm(request.POST, instance=assesorament)
        if form.is_valid():
            form.save()
            return redirect('assesorament_list')
    else:
        form = AssesoramentForm(instance=assesorament)
    
    context = {
        'form': form,
        'assesorament': assesorament
    }
    return render(request, 'edit_assesorament.html', context)
    