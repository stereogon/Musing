from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
	path('', views.home, name = 'home'),
	path('posts', views.posts, name = 'posts'),
	path('posts/<uuid:pk>', views.postPage, name = 'post_page'),
	path('about', views.about, name = 'about'),
	path('books', views.books, name = 'books'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)