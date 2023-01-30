from django.shortcuts import render, redirect
import folium 
from folium import plugins
from .models import Obec, VolebVyslPrez2023Obec1kolo, VolebVyslPrez2023Obec2kolo
from .models import Zastupitel
import json
import plotly.express as px
import pandas as pd 
from .models import Kraj
import os
import urllib.request
from urllib import request
from bs4 import BeautifulSoup
import csv
from xml.etree import ElementTree
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
# Create your views here.


def circus_mapa(request):
	map1 = folium.Map(location=[49.5, 16], tiles="CartoDB Dark_Matter", zoom_start=9)
	
	obce = Obec.objects.all()

	map1 = map1._repr_html_()

	return render(request, 'circus_mapa.html', {
		'map1': map1 

		})



def circus_volby(request):

	return render(request, 'circus_volby.html',{})



def create_csv_1_kolo(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition']= 'attachment; filename=vysl_prez_volby_23_1k.csv'

	writer = csv.writer(response)
	vysledky =  VolebVyslPrez2023Obec1kolo.objects.all()

	writer.writerow(['kraj', 'obec_cislo',
			'obec_nazev','hlasy_Fischer', 
			'hlasy_Basta', 'hlasy_Pavel', 
			'hlasy_Zima', 'hlasy_Nerudova', 
			'hlasy_Babis','hlasy_Divis', 
			'hlasy_Hilser','platne_hlasy', 
			'platne_hlasy_procenta', 'ucast_procenta',
			'zapsani_volici'])

	for vysledek in vysledky:
		writer.writerow([vysledek.cislo_kraje,
			vysledek.cislo_obce, vysledek.nazev_obce, 
			vysledek.hlasy_Fischer, vysledek.hlasy_Basta, 
			vysledek.hlasy_Pavel, vysledek.hlasy_Zima, 
			vysledek.hlasy_Nerudova, vysledek.hlasy_Babis, 
			vysledek.hlasy_Divis, vysledek.hlasy_Hilser, 
			vysledek.platne_hlasy, vysledek.plat_hlas_procenta, 
			vysledek.ucast_proc,vysledek.zapsani_volici,])

	return response



def create_csv_2_kolo(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition']= 'attachment; filename=vysl_prez_volby_23_2k.csv'

	writer = csv.writer(response)
	vysledky =  VolebVyslPrez2023Obec2kolo.objects.all()

	writer.writerow(['kraj', 'obec_cislo',
			'obec_nazev', 'hlasy_Pavel', 
			'hlasy_Babis','platne_hlasy', 
			'platne_hlasy_procenta', 'ucast_procenta',
			'zapsani_volici'])

	for vysledek in vysledky:
	
		writer.writerow([vysledek.cislo_kraje, vysledek.cislo_obce, 
			vysledek.nazev_obce, vysledek.hlasy_Pavel,
			vysledek.hlasy_Babis, vysledek.platne_hlasy, 
			vysledek.plat_hlas_procenta, vysledek.ucast_proc,
			vysledek.zapsani_volici])

	return response


def zastupitele_csv(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition']= 'attachment; filename=zastupitele_cr.csv'

	writer = csv.writer(response)
	zastupitele =  Zastupitel.objects.all()

	writer.writerow(['Jmeno', 'last_name', 'titul pred', 'titul_za', 'věk','datum narození',
		'Zastupitel', 'telefon','email', 'strana', 'Navrhující strana', 
		'Absolutní hlasy', 'Hlasy v procentech', 'funkce', 'poznamky',
		'Kod obce','kraj'])

	for zastupitel in zastupitele:
		
		writer.writerow([zastupitel.first_name, zastupitel.last_name,
			zastupitel.title, zastupitel.title_b, zastupitel.vek, zastupitel.birth_day,
			zastupitel.zastupitel, zastupitel.telefon, zastupitel.email, zastupitel.strana,
			zastupitel.navrhujici_strana, zastupitel.absolutni_hlasy, zastupitel.hlasy_v_procentech,
			zastupitel.funkce, zastupitel.poznamky, zastupitel.kod_obce, zastupitel.kraj])


	return response





def obce_csv(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition']= 'attachment; filename=obce_cr.csv'

	writer = csv.writer(response)
	obce =  Obec.objects.all()

	writer.writerow(['Obec', 'Kod obce', 'Okres', 
		'Kod okresu', 'kraj', 'PSC', 'Latitude', 
		'Longitude', 'Stranky obce'])

	for obec in obce:
		
		writer.writerow([obec.obec, obec.kod_obce, obec.okres, obec.kod_okresu,
			obec.kraj, obec.kod_kraje, obec.psc, 
			obec.latitude, obec.longitude, obec.url])


	return response