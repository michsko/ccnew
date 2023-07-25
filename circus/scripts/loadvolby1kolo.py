from info.models import VolebVyslPrez2023Obec1kolo, Kraj
import csv
import pandas as pd 
import os
from bs4 import BeautifulSoup
import urllib.request



def run():

	vsechny_kraje = Kraj.objects.get(kraj='Hlavní město Praha')

	#VolebVyslPrez2023Obec1kolo.objects.all().delete()
	
	
	
	kraj = vsechny_kraje.kod_kraje
	req = urllib.request.urlopen(f"https://www.volby.cz/pls/prez2023/vysledky_kraj?kolo=1&nuts={kraj}")

	vysledky = BeautifulSoup(req, 'xml')
	print(1)


	for item in vysledky.findAll('OBEC'):
	# 	if (obec):
		obec_cislo = item.get('CIS_OBEC')
		obec_nazev = item.get('NAZ_OBEC')
		print(item)
		hlasy_Fischer = "0"
		hlasy_Basta = "0"
		hlasy_Pavel = "0"
		hlasy_Zima = "0"
		hlasy_Nerudova = "0"
		hlasy_Babis = "0"
		hlasy_Divis = "0"
		hlasy_Hilser = "0"


		# untested match case version
		
		match item:
		    case item.findAll('HODN_KAND', {'PORADOVE_CISLO': '1'}):
		        hlasy_Fischer = vysledek.get('HLASY')
		    case item.findAll('HODN_KAND', {'PORADOVE_CISLO': '2'}):
			hlasy_Basta = vysledek.get('HLASY')
		    case item.findAll('HODN_KAND', {'PORADOVE_CISLO': '4'}):				
			hlasy_Pavel = vysledek.get('HLASY')
		    case item.findAll('HODN_KAND', {'PORADOVE_CISLO': '5'}):
			hlasy_Zima = vysledek.get('HLASY')
		    case item.findAll('HODN_KAND', {'PORADOVE_CISLO': '6'}):
			hlasy_Nerudova = vysledek.get('HLASY')
		    case item.findAll('HODN_KAND', {'PORADOVE_CISLO': '7'}):
		        hlasy_Babis = vysledek.get('HLASY')
		    case item.findAll('HODN_KAND', {'PORADOVE_CISLO': '8'}):
		        hlasy_Divis = vysledek.get('HLASY')
		    case item.findAll('HODN_KAND', {'PORADOVE_CISLO': '9'}):
		        hlasy_Hilser = vysledek.get('HLASY')

		
		"""
		for vysledek in item.findAll('HODN_KAND', {'PORADOVE_CISLO': '1'}):
			hlasy_Fischer = vysledek.get('HLASY')

		for vysledek in item.findAll('HODN_KAND', {'PORADOVE_CISLO': '2'}):
			hlasy_Basta = vysledek.get('HLASY')

		for vysledek in item.findAll('HODN_KAND', {'PORADOVE_CISLO': '4'}):																											
			hlasy_Pavel = vysledek.get('HLASY')

		for vysledek in item.findAll('HODN_KAND', {'PORADOVE_CISLO': '5'}):	
			hlasy_Zima = vysledek.get('HLASY')

		for vysledek in item.findAll('HODN_KAND', {'PORADOVE_CISLO': '6'}):
			hlasy_Nerudova = vysledek.get('HLASY')

		for vysledek in item.findAll('HODN_KAND', {'PORADOVE_CISLO': '7'}):
			hlasy_Babis = vysledek.get('HLASY')

		for vysledek in item.findAll('HODN_KAND', {'PORADOVE_CISLO': '8'}):
			hlasy_Divis = vysledek.get('HLASY')

		for vysledek in item.findAll('HODN_KAND', {'PORADOVE_CISLO': '9'}):
			hlasy_Hilser = vysledek.get('HLASY')
			
"""
		for vysledek in item.findAll('UCAST'):
		
			platne_hlasy = vysledek.get('PLATNE_HLASY')
			platne_hlasy_procenta = vysledek.get('PLATNE_HLASY_PROC')
			ucast_procenta = vysledek.get('UCAST_PROC')
			zapsani_volici = vysledek.get('ZAPSANI_VOLICI')

		print(item)

		print(kraj, obec_cislo, obec_nazev, 
			hlasy_Fischer, hlasy_Basta, hlasy_Pavel, 
			hlasy_Zima, hlasy_Nerudova, hlasy_Babis, 
			hlasy_Divis, hlasy_Hilser, ucast_procenta, 
			platne_hlasy, platne_hlasy_procenta, ucast_procenta,
			zapsani_volici,)


		VolebVyslPrez2023Obec1kolo.objects.create(cislo_kraje=kraj, cislo_obce=obec_cislo,
			nazev_obce=obec_nazev, hlasy_Fischer= hlasy_Fischer, 
			hlasy_Basta=hlasy_Basta, hlasy_Pavel=hlasy_Pavel, 
			hlasy_Zima=hlasy_Zima, hlasy_Nerudova=hlasy_Nerudova, 
			hlasy_Babis=hlasy_Babis, hlasy_Divis=hlasy_Divis, 
			hlasy_Hilser=hlasy_Hilser, platne_hlasy=platne_hlasy, 
			plat_hlas_procenta=platne_hlasy_procenta, ucast_proc=ucast_procenta,
			zapsani_volici=zapsani_volici)















