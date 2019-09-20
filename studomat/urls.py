"""studomat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from index.views import index_render
from administrator.views import admin_render, dodavanje_osobe, brisanje_profesora, brisanje_studenta
from profesor.views import prof_render
from student.views import stud_render
from redirect.views import redirect_render;
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', index_render),
    path('redirect/', redirect_render),
    path('administrator/', admin_render),
    path('profesor/', prof_render),
    path('student/', stud_render),
    path('dodavanje/', dodavanje_osobe),
    path('brisanjeStudent/<str:studjmbag>/', brisanje_studenta),
    path('brisanjeProfesor/<str:profjmbag>/', brisanje_profesora),
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
]
