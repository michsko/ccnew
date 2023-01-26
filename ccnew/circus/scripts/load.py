from info.models import Obec,Kraj
import csv
import pandas as pd 
import os

def run():
	file = open('scripts/souradnice.csv')
	next(file)
	read_file=csv.reader(file)
		
	#Obec.objects.all().delete()


	for record in read_file:
		print(record[5])
		kraj = Kraj.objects.get(kod_kraje=record[5])

		Obec.objects.create(obec=record[0], kod_obce=record[1], okres=record[2], 
				kod_okresu=record[3], kraj=record[4], kod_kraje=kraj, psc=record[6], 
				latitude=record[7], longitude=record[8])
		print(record)

		

