from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Blog(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=50)
	content = models.TextField(max_length=500)
	date = models.DateTimeField(auto_now_add=True)
	modified_date= models.DateTimeField(auto_now_add=True, editable=True)
	
	def __str__(self):
		return self.title

class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.CharField(max_length=100)
	date = models.DateTimeField(auto_now_add=True)
	related_post = models.ForeignKey(Blog, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.content



