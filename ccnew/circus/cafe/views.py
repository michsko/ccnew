from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile, User
from django.contrib import messages

# Create your views here.

def index(request):
	return render(request, 'index.html',{})


def profile_list(request):
	if request.user.is_authenticated: 
		profiles = Profile.objects.exclude(user=request.user)
		return render(request, 'profile_list.html', {
			'profiles': profiles,
			}) 
	else: 
		messages.success(request, ('Vidět profily uživatelů můžete až po přihlášení.'))
		return redirect('login')


def profile(request, pk):
	if request.user.is_authenticated:
		profile = Profile.objects.get(user_id=pk)

		if request.method == "POST": 
			current_user_profile = request.user.profile
			action = request.POST['follow']
			
			if action == "unfollow": 
				current_user_profile.follows.remove(profile)
			elif action == "follow":
				current_user_profile.follows.add(profile)
				current_user_profile.save()

		return render(request, 'profile.html', {
			'profile': profile, 
			})
	else: 
		messages.success(request, ('Vidět profil uživatele můžete až po přihlášení.'))
		return redirect('login')