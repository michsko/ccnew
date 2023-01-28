from django.shortcuts import render, redirect
import folium 
from folium import plugins
from .models import Obec
import json
# Create your views here.

def circus_mapa(request):
	map1 = folium.Map(location=[49.5, 16], tiles="CartoDB Dark_Matter", zoom_start=9)
	
	obce = Obec.objects.all()

	map1 = map1._repr_html_()

	return render(request, 'circus_mapa.html', {
		'map1': map1 

		})



def circus_volby(request):
	
	volebni_okrsky = json.load(open('info/static/json/volebni_okrsky-simple.json', 'r'))
	print(volebni_okrsky['features'][0])
	
	return render(request, 'circus_volby.html',{})

