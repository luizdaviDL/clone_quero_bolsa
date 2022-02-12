from django import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('detalhes<int:id>', views.detalhes, name='detalhes'),
   path('garantir_bolsa<int:id>', views.garantir_bolsa, name='garantir_bolsa'),
   path('cadastro_bolsa<int:id>', views.cadastro_bolsa, name='cadastro_bolsa'),
]
