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
from django.views.generic import RedirectView

from music_engine.views import *

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('studios/', StudioListView.as_view(), name='studio_list'),
    path('studio/<str:pk>/', studio_detail, name='studio_detail'),
    path('materials/', MaterialListView.as_view(), name='material_list'),
    path('material/<str:pk>/', material_detail, name='material_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
]
