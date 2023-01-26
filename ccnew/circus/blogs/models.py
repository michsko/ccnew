from django.db import models
from django.utils.timezone import now
# Create your models here.

class BlogPost(models.Model):
	name = models.CharField('Název', max_length=255)
	owner = models.IntegerField("Majitel", blank=False, default=1)
	title = models.CharField('Titulek',max_length=255)
	author = models.CharField('Autor',max_length=255)
	date_published = models.DateTimeField(default=now,  editable=True)
	likes = models.IntegerField("Líbí se", blank=False, default=0)
	read = models.IntegerField("Přečteno", blank=False, default=-0)
	content = models.TextField(blank=False)
	theme = models.TextField(blank=False,)

	def __str__(self):
		return self.name