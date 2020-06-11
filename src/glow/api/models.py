from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Blog(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=50)
	content = models.TextField(max_length=500)
	author = models.CharField(max_length=100)
	date = models.DateTimeField(auto_now_add=True)
	modified_date= models.DateTimeField(auto_now=True)

class Comments(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.CharField(max_length=100)
