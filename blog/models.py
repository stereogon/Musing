import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
	category_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
	name = models.CharField(max_length = 50)

	def __str__(self):
		return self.name

class Post(models.Model):
	post_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
	title = models.CharField(max_length = 200)
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	category = models.ForeignKey(Category, on_delete = models.SET_NULL, null = True)
	body = models.TextField()
	thumbnail = models.ImageField(upload_to = 'thumbnails', null=True, blank=True)
	created_on = models.DateTimeField(auto_now_add = True)
	modified_on = models.DateTimeField(auto_now = True)

	def __str__(self):
		if len(self.title)<=40:
			return self.title
		else:
			return self.title[0:40] + '...'

	class Meta:
		ordering = ['-created_on', '-modified_on']

class Comment(models.Model):
	comment_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
	post = models.ForeignKey(Post, on_delete = models.CASCADE, null = True, blank = True)
	name = models.CharField(max_length = 50)
	body = models.TextField()
	created_on = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.body[0:50]

	class Meta:
		ordering = ['-created_on']