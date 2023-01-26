from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm


# Create your views here.

def login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
	
		if user is not None: 
			login(request, user)
			messages.success(request, ('Vaše přihlášení proběhlo úspěšně.'))
			return redirect('index')
			  
		else: 
			messages.success(request, ('Něco se nepovedlo, prosím zkuste to znovu.'))
			return redirect('login_user')
	else: 
		return render(request, 'authenticate/login_user.html',{}) 


def logout_user(request):
	logout(request)
	messages.success(request, ('Byly jste odhlášeni.'))
	return redirect('index')
	


def register_user(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ('Vaše registrace byla úspěšně dokončena.'))
			return redirect('index')
		else:
			messages.error(request, form.errors)

	else:
		form = UserRegisterForm() 
	
	return render(request, 'authenticate/register_user.html', {
		'form': form, 
		})