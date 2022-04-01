from django.contrib import admin
from .models import Post, Category, Comment


# Register your models here.
admin.site.register(Category)
admin.site.register(Comment)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	class Media:
		js = ('js/tinyInject.js',)