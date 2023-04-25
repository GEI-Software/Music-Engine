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
    path('llista-tecnics/', LlistaTecnics.as_view(), name='llista_tecnics'),
    path("create/studio/", StudioCreate.as_view()),
    path('studio/<str:pk>/delete/', StudioDelete.as_view(), name='studio_delete'),
    path("create/material/", MaterialCreate.as_view()),
    path('material/<str:pk>/delete/', MaterialDelete.as_view(), name='material_delete'),
    path('material/<str:pk>/edit',
         MaterialUpdate.as_view(model=MusicalMaterial, form_class=MaterialForm),
         name='material_edit'),
    path('hours/', HoursListView.as_view(), name='hours_list'),
    path("create/hour_record/", HourRecordCreate.as_view()),
]
