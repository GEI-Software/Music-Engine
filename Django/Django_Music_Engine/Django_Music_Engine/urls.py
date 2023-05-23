"""Django_Music_Engine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from music_engine.views import *
from music_engine.forms import *


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('studios/', StudioListView.as_view(), name='studio_list'),
    path('studio/<str:pk>/', studio_detail, name='studio_detail'),
    path('assignments/', AssignmentListView.as_view(), name='assignment_list'),
    path('materials/', MaterialListView.as_view(), name='material_list'),
    path('material/<str:pk>/', material_detail, name='material_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('studio/<str:pk>/edit',
         StudioUpdate.as_view(model=MusicalStudio, form_class=StudioForm),
         name='studio_edit'),
    path('reserves/', ReservaListView.as_view(), name='reserva_list'),
    path('reserves/<int:pk>/', reserva_detail, name='reserva_detail'),
    path("create/reserva/", ReservaCreate.as_view()),
    path('llista-tecnics/', LlistaTecnics.as_view(), name='llista_tecnics'),
    path('caracteristiques/',CharacteristicTechinicalPersonview.as_view(),name='characteristic_technical'),
    path("create/studio/", StudioCreate.as_view()),
    path('studio/<str:pk>/delete/', StudioDelete.as_view(), name='studio_delete'),
    path("create/material/", MaterialCreate.as_view()),
    path('material/<str:pk>/delete/', MaterialDelete.as_view(), name='material_delete'),
    path('material/<str:pk>/edit',
         MaterialUpdate.as_view(model=MusicalMaterial, form_class=MaterialForm),
         name='material_edit'),
    path('hours/', HoursListView.as_view(), name='hours_list'),
    path("create/hour_record/", HourRecordCreate.as_view()),
    path('update/<int:pk>/hour/', HourUpdateView.as_view(), name='hours_update'),
    path('delete/<int:pk>/hour/', HourDeleteView.as_view(), name='hours_delete'),
    path('dades/',ReceipListView.as_view(), name='financial_data_list'),
    path('dades/<int:pk>/',ReceipDetailView.as_view(), name='financial_data_detail'),
    path('dades/create/', ReceipCreateView.as_view(), name='financial_data_create'), #Check view
    path('dades/<int:pk>/update/', ReceipUpdateView.as_view(), name='financial_data_update'),
    path('dades/<int:pk>/delete/', ReceipDelateView.as_view(), name='financial_data_delete'),
    path('calendario/', calendario_tecnico , name='calendario'),
    path('disponibilidad/<int:year>/<int:month>/<int:day>/', disponibilidad_tecnico, name='disponibilidad'),
    path('serveis/', serveis, name='serveis'),
    path('assesoraments/', assesorament_list, name='assesorament_list'),
    path('assesoraments/create/', create_assesorament, name='create_assesorament'),
    path('assesoraments/edit/<int:assesorament_id>/', edit_assesorament, name='edit_assesorament'),
    path("toggle-state/<int:pk>/", toggle_state, name="toggle_state"),
    path("toggle-state-fd/<int:pk>/", toggle_state_fd, name="toggle_state_fd"),
    path('', material_list_client, name='material_list_client'),
    path('<str:name>/', material_detail_client, name='material_detail_client'),
    path('<str:name>/reserve/', reserve_material, name='reserve_material')

]