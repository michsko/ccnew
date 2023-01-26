from django import forms
from django.forms import ModelForm
from .models import BlogPost



class BlogPostForm(forms.ModelForm):
	class Meta: 
			model = BlogPost
			fields = ['name', 'title', 'theme', 'content',]
			labels = {'name': 'Název', 'title': 'Titulek', 'content': 'Příspěvek', 'theme': 'Téma',}
			widgets={'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Zkrácený název pomahá ve vyhledávaní článku.'}),
		'title': forms.TextInput(attrs={'class': 'form-control',}),
		'theme': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Téma pomáha k orientaci při vyhledávaní.'}),
		'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Zde je místo pro váš článek.'})}


		