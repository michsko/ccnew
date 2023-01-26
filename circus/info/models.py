from django.db import models
from django.contrib import admin 

# Create your models here.

class KrajAdmin(admin.ModelAdmin):
	search_fields = ['Kraj', 'kod Kraje','Stranky kraje'] 
	
class Kraj(models.Model):
	kraj = models.CharField('Kraj', max_length=255)
	kod_kraje = models.CharField('kod kraje', max_length=255)
	latitude = models.FloatField('Latitude', max_length=255)
	longitude = models.FloatField('Longitude', max_length=255)
	url = models.URLField('Stranky kraje', max_length=255)


	def __str__(self):
		return "%s %s" % (self. kraj, self.kod_kraje)

class ObecAdmin(admin.ModelAdmin):
	search_fields = ['obec', 'kod_obce','okres','kod_okresu','kraj', 'psc','url'] #add the fields you want to search
	

class Obec(models.Model):
	obec = models.CharField('Obec', max_length=255)
	kod_obce = models.CharField('Kod obce', max_length=255)
	okres = models.CharField('Okres', max_length=255)
	kod_okresu = models.CharField('Kod okresu', max_length=255)
	kraj = models.CharField('kraj', max_length=255)
	kod_kraje = models.ForeignKey(Kraj, on_delete=models.CASCADE)
	psc = models.CharField('PSC', max_length=255)
	latitude = models.FloatField('Latitude', max_length=255)
	longitude = models.FloatField('Longitude', max_length=255)
	url = models.URLField('Stranky obce', max_length=255)

	

	def __str__(self):
		return self.obec

class ZastupitelAdmin(admin.ModelAdmin):
	search_fields = ['first_name', 'last_name', 'vek','title','telefon','email', 'strana',
	'funkce', 'poznamky', 'birth_day', 'obec__obec', 'kraj'] 

class Zastupitel(models.Model):
	first_name = models.CharField('Jmeno', max_length=255)
	last_name = models.CharField('Prijmeni', max_length=255)
	title = models.CharField('Titul', max_length=255, blank=True)
	title_b = models.CharField('Titul za', max_length=255, blank=True)
	vek = models.CharField('věk', blank=True, max_length=255)
	birth_day = models.CharField('den narození', max_length=255, blank=True)
	zastupitel = models.BooleanField('Zastupitel', default=True)
	telefon = models.CharField('telefon', max_length=255, blank=True)
	email = models.EmailField('email', blank=True)
	strana = models.CharField('strana', max_length=255, blank=True)
	navrhujici_strana = models.CharField('Navrhující strana', max_length=255, blank=True)
	absolutni_hlasy = models.CharField('Absolutní hlasy', max_length=255, blank=True)
	hlasy_v_procentech = models.CharField('Hlasy v procentech', max_length=255, blank=True)
	funkce = models.CharField('funkce', max_length=255, blank=True)
	poznamky = models.TextField('poznamky', blank=True)
	kod_obce = models.CharField('Kod obce', max_length=255, blank=True)
	kraj = models.CharField('kraj', max_length=255, default="p")
	obec = models.ForeignKey(Obec, on_delete=models.CASCADE)

	def __str__(self):
 		return "%s %s %s" % (self.title, self.last_name, self.first_name)

class ZastupitelKrajeAdmin(admin.ModelAdmin):
	search_fields = ['first_name', 'last_name','vek','title','telefon','email', 'strana', 'funkce', 'poznamky', 'birth_day', 'birth_month', 'birth_year']
	
class ZastupitelKraje(models.Model):
	first_name = models.CharField('Jmeno', max_length=255)
	last_name = models.CharField('Prijmeni', max_length=255)
	title = models.CharField('Titul', max_length=255, blank=True)
	title_b = models.CharField('Titul za', max_length=255, blank=True)
	vek = models.CharField('věk', blank=True, max_length=255)
	birth_day = models.CharField('den narození', max_length=255, blank=True)
	zastupitel = models.BooleanField('Zastupitel', default=True)
	telefon = models.CharField('telefon', max_length=255, blank=True)
	email = models.EmailField('email', blank=True)
	strana = models.CharField('strana', max_length=255, blank=True)
	navrhujici_strana = models.CharField('Navrhující strana', max_length=255, blank=True)
	absolutni_hlasy = models.CharField('Absolutní hlasy', max_length=255, blank=True)
	hlasy_v_procentech = models.CharField('Hlasy v procentech', max_length=255, blank=True)
	funkce = models.CharField('funkce', max_length=255, blank=True)
	poznamky = models.TextField('poznamky', blank=True)
	kod_kraje = models.CharField('kod kraje', max_length=255, blank=True)
	kraj = models.ForeignKey(Kraj, on_delete=models.CASCADE)

	def __str__(self):
 		return "%s %s %s" % (self.title, self.last_name, self.first_name)


