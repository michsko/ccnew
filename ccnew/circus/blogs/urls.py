from django.urls import path
from . import views 

urlpatterns=[
	path('blog_posts/<blogpost_owner>', views.blog_posts, name='blog_posts'),
	path('blog_add', views.blog_add, name='blog_add'),
	path('blog_post/<blogpost_id>', views.blog_post, name='blog_post'),
	path('blog_post_edit/<blogpost_id>', views.blog_post_edit, name='blog_post_edit'),
	path('blog_post_delete/<blogpost_id>', views.blog_post_delete, name='blog_post_delete'), 
]

