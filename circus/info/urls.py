from django.urls import path
from . import views

urlpatterns=[

path('circus_mapa', views.circus_mapa, name='circus_mapa'),
path('circus_volby', views.circus_volby, name='circus_volby'),
path('create_csv_1_kolo', views.create_csv_1_kolo, name='create_csv1'),
path('create_csv_2_kolo', views.create_csv_2_kolo, name='create_csv2'),
path('zastupitele_csv', views.zastupitele_csv, name='zastupitele_csv'),
path('obce_csv', views.obce_csv, name='obce_csv'),




]