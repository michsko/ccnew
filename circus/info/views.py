from django.shortcuts import render, redirect
import folium 
from folium import plugins
from .models import Obec
import json
import plotly.express as px
import pandas as pd 
from .models import Kraj
import os
import urllib.request
from bs4 import BeautifulSoup
# Create your views here.

def circus_mapa(request):
	map1 = folium.Map(location=[49.5, 16], tiles="CartoDB Dark_Matter", zoom_start=9)
	
	obce = Obec.objects.all()

	map1 = map1._repr_html_()

	return render(request, 'circus_mapa.html', {
		'map1': map1 

		})



def circus_volby(request):

	vsechny_kraje = Kraj.objects.all()

	for kraj in vsechny_kraje:
		kod_kraje = kraj.kod_kraje	
		req = urllib.request.urlopen(f"https://www.volby.cz/pls/prez2023/vysledky_kraj?kolo=&nuts={kod_kraje}")

		vysledky = BeautifulSoup(req, 'xml')


	#vysledky kraj
		for item in vysledky.findAll('KRAJ'):
			# nazev_kraje = item['NAZ_KRAJ']
				
			print(item)
	#vysledky kraj konec


	#vysledky okres
	# 	for item in vysledky.findAll('OKRES'):
	# 		nazev_okresu = item['NAZ_OKRES']
	# 		kandidat = item["PORADOVE_CISLO"]
	# 		kandidat_hlasy = item['HLASY']		
	# 		print(nazev_okresu, kandidat, kandidat_hlasy)
	# #vysledky okres konec


	#vysledky obec 
		for item in vysledky.findAll('OBEC'):
	# 		nazev_obce = item['NAZ_OBEC']
	# 		kandidat = item["PORADOVE_CISLO"]
	# 		kandidat_hlasy = item['HLASY']		
	 		print(item)
	# #vysledky obec konec
			

	# ucast 
		# for item in volebni_okrsky.findAll('UCAST'):
		# 	okrsky_celkem = item['OKRSKY_CELKEM']
		# 	okrsky_zpracovane = item['OKRSKY_ZPRAC']
		# 	okrsky_zpracovane_proc = item['OKRSKY_ZPRAC_PROC']
		# 	zapsani_volici = item['ZAPSANI_VOLICI']
		# 	ucast_proc = item["UCAST_PROC"]
		# 	print(okrsky_celkem, okrsky_zpracovane, okrsky_zpracovane_proc, zapsani_volici, ucast_proc) 
		
			
	#ucast konec
		
	okrsky_id_map = {}
	
	volebni_okrsky = json.load(open('info/static/json/volebni_okrsky-simple.json', 'r'))
	for feature in volebni_okrsky['features']:
		feature['id'] = feature['properties']['KOD']
	
		okrsky_id_map[feature['properties']['OBEC_KOD']] = feature['id']
	
	data = pd.read('')

	px.choropleth(data, locations='id', geojson='volebni_okrsky', color='babis/pavel', )
	

	
	return render(request, 'circus_volby.html',{})

