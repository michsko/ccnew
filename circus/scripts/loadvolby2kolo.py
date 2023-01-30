from info.models import VolebVyslPrez2023Obec2kolo, Kraj
import csv
import pandas as pd 
import os
from bs4 import BeautifulSoup
import urllib.request



def run():

	vsechny_kraje = Kraj.objects.get(kraj='Jihočeský kraj')

	#VolebVyslPrez2023Obec2kolo.objects.all().delete()

	kraj = vsechny_kraje.kod_kraje
	req = urllib.request.urlopen(f"https://www.volby.cz/pls/prez2023/vysledky_kraj?kolo=2&nuts={kraj}")

	vysledky = BeautifulSoup(req, 'xml')
	print(1)


	for item in vysledky.findAll('OBEC'):
	
		obec_cislo = item.get('CIS_OBEC')
		obec_nazev = item.get('NAZ_OBEC')
		print(item)
		
		hlasy_Pavel = "0"
		hlasy_Babis = "0"

		for vysledek in item.findAll('HODN_KAND', {'PORADOVE_CISLO': '4'}):
			hlasy_Pavel = vysledek.get('HLASY')

		
		for vysledek in item.findAll('HODN_KAND', {'PORADOVE_CISLO': '7'}):
			hlasy_Babis = vysledek.get('HLASY')

		for vysledek in item.findAll('UCAST'):
		
			platne_hlasy = vysledek.get('PLATNE_HLASY')
			platne_hlasy_procenta = vysledek.get('PLATNE_HLASY_PROC')
			ucast_procenta = vysledek.get('UCAST_PROC')
			zapsani_volici = vysledek.get('ZAPSANI_VOLICI')


		print(kraj, obec_cislo, obec_nazev, hlasy_Pavel, hlasy_Babis, ucast_procenta, 
			platne_hlasy, platne_hlasy_procenta, ucast_procenta, zapsani_volici,)


		VolebVyslPrez2023Obec2kolo.objects.create(cislo_kraje=kraj, cislo_obce=obec_cislo,nazev_obce = obec_nazev,
			hlasy_Pavel=hlasy_Pavel, hlasy_Babis=hlasy_Babis, platne_hlasy=platne_hlasy, 
			plat_hlas_procenta=platne_hlasy_procenta, ucast_proc=ucast_procenta,
			zapsani_volici=zapsani_volici)



