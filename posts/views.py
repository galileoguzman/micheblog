from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Post

@login_required(login_url='/admin/login/')
def home(request):
	posts = Post.objects.all()
	return render(request, 'posts_list.html', {'posts': posts})