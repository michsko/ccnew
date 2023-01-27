from django.urls import path
from . import views



urlpatterns=[

path('circus_mapa', views.circus_mapa, name='circus_mapa'),
path('circus_volby', views.circus_volby, name='circus_volby'),

]