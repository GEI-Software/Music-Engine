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
from django.urls import path, include, re_path
from music_engine.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', StudioListView.as_view(), name='studio_list'),
    path('studio/<int:pk>/', studio_detail, name='studio_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    re_path("^accounts/login/$", include('django.contrib.auth.urls'), name='login'),
    re_path("^accounts/logout/$", include('django.contrib.auth.urls'), name='logout'),
    re_path("^accounts/password_change/$", include('django.contrib.auth.urls'), name='password_change'),
    re_path("^accounts/password_change/done/$", include('django.contrib.auth.urls'), name='password_change_done'),
    re_path("^accounts/password_reset/$", include('django.contrib.auth.urls'), name='password_reset'),
    re_path("^accounts/password_reset/done/$", include('django.contrib.auth.urls'), name='password_reset_done'),
    re_path("^accounts/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Zaz]{1,"
            "20})/$", include('django.contrib.auth.urls'), name='password_reset_confirm'),
    re_path("^accounts/reset/done/$", include('django.contrib.auth.urls'), name='password_reset_complete'),

]
