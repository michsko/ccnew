from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import BlogPost
from .forms import BlogPostForm
from datetime import datetime


# Create your views here.


def blog_posts(request, blogpost_owner):
	blog_posts = BlogPost.objects.all().order_by('-date_published').filter(owner=blogpost_owner)
	return render(request, 'blogs.html', {
		'blog_posts': blog_posts,
		})

def blog_add(request):
	submitted = False
	if request.method == 'POST':
		form = BlogPostForm(request.POST)
		if form.is_valid():
			blog_post = form.save(commit=False)
			blog_post.author = request.user.username
			blog_post.owner = request.user.id
			blog_post.save()
			messages.success(request,('Váš příspěvek byl přidán.'))
			return redirect("blog_posts", blogpost_owner=blog_post.owner)
	else:
		form = BlogPostForm
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'blog_add.html', {
		'form': form, 
		'submitted': submitted,
		})


def blog_post(request, blogpost_id):
	blog_post = BlogPost.objects.get(pk=blogpost_id)
	return render(request, 'blog.html', {
		'blog_post': blog_post,
		})


def blog_post_edit(request, blogpost_id):
	blog_post = BlogPost.objects.get(pk=blogpost_id)
	form = BlogPostForm(request.POST or None, instance=blog_post)
	if form.is_valid():
			form.save()
			messages.success(request, ('Váš příspěvek byl upraven.'))
			return redirect('blog_posts', blogpost_owner=blog_post.owner)


	return render(request, 'blog_post_edit.html', {
		'form': form,
		'blog_post': blog_post,
		})


def blog_post_delete(request, blogpost_id):
	blog_post = BlogPost.objects.get(pk=blogpost_id)
	blog_post.delete()
	messages.success(request, ("Váš příspěvek byl smazán."))
	return redirect('blog_posts', blogpost_owner=blog_post.owner)