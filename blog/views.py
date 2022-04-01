from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Category, Comment
from django.db.models import Q
from django.contrib.auth.models import User
from django.core.paginator import Paginator
# Create your views here.


def home(request):
	context = {}

	q = request.GET.get('q') if request.GET.get('q') != None else ''
	posts = Post.objects.filter(
		Q(title__icontains = q) |
		Q(category__name__icontains = q) |
		Q(body__icontains = q)
	)

	g = True
	if q=='':
		g = False

	context['g'] = g

	if len(posts)>4:
		context['posts'] = posts[0:4]
	else:
		context['posts'] = posts

	if len(posts)==0:
		context['no_post'] = True
	else:
		context['no_post'] = False

	return render(request, 'blog/home.html', context)

def posts(request):
	context = {}
	categories = Category.objects.all()[0:8]
	q = request.GET.get('q') if request.GET.get('q') != None else ''
	posts = Post.objects.filter(
		Q(title__icontains = q) | 
		Q(category__name__icontains = q) |
		Q(body__icontains = q)
	)

	g = True
	if q=='':
		g = False

	context['g'] = g
	if len(posts)==0:
		context['no_post'] = True
	else:
		context['no_post'] = False

	p = Paginator(posts, 8)
	page = request.GET.get('page')
	posts_on_page = p.get_page(page)

	context['posts_on_page'] = posts_on_page
	context['posts'] = posts
	context['categories'] = categories

	return render(request, 'blog/posts.html', context)

def postPage(request, pk):
	context = {}
	post = Post.objects.get(post_id = pk)

	if request.method == 'POST':
		name = request.POST.get('name')
		body = request.POST.get('body')
		c = Comment(post = post, name = name, body = body)
		c.save()

		return redirect('/posts/' + str(pk))

	comments = Comment.objects.filter(
		Q(post__post_id = str(pk))
	)

	categories = Category.objects.all()

	context['categories'] = categories
	context['comments'] = comments
	context['post'] = post
	return render(request, 'blog/post_page.html', context)

def about(request):
	return render(request, 'blog/about.html')

def books(request):
	context = {}
	q = request.GET.get('q') if request.GET.get('q') != None else ''

	posts = Post.objects.filter(
		Q(category__name = 'Books') &
		(Q(title__icontains = q) | 
		Q(category__name__icontains = q) |
		Q(body__icontains = q))
	)

	g = True
	if q=='':
		g = False

	context['g'] = g

	if len(posts)==0:
		context['no_post'] = True
	else:
		context['no_post'] = False

	p = Paginator(posts, 8)
	page = request.GET.get('page')

	if page is None:
		page = 1

	posts_on_page = p.get_page(page)

	context['posts'] = posts
	context['posts_on_page'] = posts_on_page
	return render(request, 'blog/books.html', context)