from rest_framework import serializers
from .models import Blog, Comment
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):

	class Meta:
		model = Blog
		fields = [
		'user',
		'title',
		'content',
		'date',
		'modified_date'
		]

class CommentSerializer(serializers.ModelSerializer):

	class Meta:
		model = Comment
		fields = [
		'user',
		'content',
		'date',
		]