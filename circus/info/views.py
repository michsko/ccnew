from django.shortcuts import render, redirect
import folium 
from folium import plugins
from .models import Obec
# Create your views here.

def circus(request):
	map1 = folium.Map(location=[49.5, 16], tiles="CartoDB Dark_Matter", zoom_start=9)
	
	obce = Obec.objects.all()

	map1 = map1._repr_html_()

	return render(request, 'circus.html', {
		'map1': map1 

		})

