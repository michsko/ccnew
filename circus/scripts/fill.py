from bs4 import BeautifulSoup
from info.models import Zastupitel, Obec
import urllib.request

def run():
	
	Zastupitel.objects.all().filter(first_name=name, last_name=)

	vsechny_obce = Obec.objects.all().filter(kraj='Jihočeský kraj')
	
	for obec in vsechny_obce:
		kod_obce = obec.kod_obce	
		kraj = obec.kraj 
		req = urllib.request.urlopen(f"https://www.volby.cz/pls/kv2022/vysledky_obec?datumvoleb=20220923&cislo_obce={kod_obce}")

		person = BeautifulSoup(req, 'xml')

		for item in person.findAll('ZASTUPITEL'):
			jmeno = item['JMENO']
			prijmeni = item['PRIJMENI']
			titul = item['TITULPRED']
			titul_b = item['TITULZA']
			hlasy = item['HLASY']
			hlasy_proc = item['HLASY_PROC']

			print(jmeno, prijmeni, titul, titul_b, hlasy, hlasy_proc, kraj) 
		
			Zastupitel.objects.create(first_name = jmeno, last_name = prijmeni, 
				title = titul, title_b = titul_b, absolutni_hlasy = hlasy, 
				hlasy_v_procentech = hlasy_proc, obec = obec, kod_obce=kod_obce,
				kraj=kraj)
